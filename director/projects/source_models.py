import enum
import mimetypes
import typing
from io import BytesIO
from os.path import splitext

from allauth.socialaccount.models import SocialToken
from django.contrib.contenttypes.models import ContentType
from django.core.files import File
from django.core.files.base import ContentFile
from django.db import models
from django.urls import reverse
from polymorphic.models import PolymorphicModel


class MimeTypeDetectMixin(object):
    path: str
    source: typing.Any

    @property
    def mimetype(self) -> str:
        if hasattr(self, 'source') and self.source is not None and hasattr(self.source, 'mimetype'):
            mimetype = self.source.mimetype
            if mimetype and mimetype != 'Unknown':
                return mimetype

        if self.path.lower().endswith('.jats.xml'):
            return 'text/xml+jats'

        mimetype, encoding = mimetypes.guess_type(self.path, False)

        if not mimetype:
            name, ext = splitext(self.path)

            if ext.lower() == '.md':
                return 'text/markdown'
            elif ext.lower() == '.rmd':
                return 'text/rmarkdown'
            elif ext.lower() == '.ipynb':
                return 'application/x-ipynb+json'

        return mimetype or 'Unknown'


class DiskSource(object):
    """Not a Source that is stored in the database but used in directory listing for files that are already on disk."""

    type = 'disksource'  # emulate PolymorphicModel type property
    type_id = 'disk'

    def to_json(self) -> dict:
        return {
            'type_id': self.type_id
        }


class Source(PolymorphicModel, MimeTypeDetectMixin):
    provider_name = ''
    type_id = ''

    project = models.ForeignKey(
        'Project',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='sources'
    )

    path = models.TextField(
        null=False,
        default='.',
        help_text='The path that the file or directory from the source is mapped to in the project'
    )

    updated = models.DateTimeField(
        auto_now=True,
        help_text='Time this model instance was last updated'
    )

    def __str__(self) -> str:
        return "Source {}".format(self.path)

    @property
    def description(self) -> str:
        """Not very useful, subclasses should override this to provide something more meaningful."""
        return str(self)

    @property
    def type(self) -> typing.Type['Source']:
        return ContentType.objects.get_for_id(self.polymorphic_ctype_id).model

    def get_absolute_url(self):
        return reverse('source_detail', args=[self.type_id, self.pk])

    def pull(self) -> BytesIO:
        raise NotImplementedError('Pull is not implemented for class {}'.format(self.__class__.__name__))

    def push(self, archive: typing.Union[str, typing.IO]) -> None:
        raise NotImplementedError('Push is not implemented for class {}'.format(self.__class__.__name__))


# Source classes in alphabetical order
#
# Note: many of these are, obviously, not implemented, but have
# been added here as placeholders, to sketch out the different types of
# project sources that might be available
#
# Note: where these derived classes do not need any additional
# fields you can use `class Meta: abstract = True`
# so that an additional database table is not created.
# However, that means that they are not available in the admin.


class BitbucketSource(Source):
    """A project hosted on Bitbucket."""

    provider_name = 'BitBucket'
    type_id = 'bitbucket'

    class Meta:
        abstract = True


class DatSource(Source):
    """A project hosted on Dat."""

    provider_name = 'Dat'
    type_id = 'dat'

    class Meta:
        abstract = True


class DropboxSource(Source):
    """A project hosted on Dropbox."""

    provider_name = 'Drop Box'
    type_id = 'dropbox'

    class Meta:
        abstract = True


def files_source_file_path(instance: "FileSource", filename: str):
    # File will be uploaded to MEDIA_ROOT/files_projects/<id>/<filename>
    return 'projects/{0}/{1}'.format(instance.id, filename)


class FileSource(Source):
    """A file uploaded to the Hub."""

    provider_name = 'File'
    type_id = 'file'

    size = models.IntegerField(
        null=True,
        blank=True,
        help_text='Size of the file in bytes'
    )

    file = models.FileField(
        null=False,
        blank=True,
        upload_to=files_source_file_path,
        help_text='The actual file stored'
    )

    def save(self, *args, **kwargs):
        """Override of base superclass `save` method to update the size property from the file size."""
        if self.file:
            self.size = self.file.size
        super().save(*args, **kwargs)

    def pull(self):
        """Pull the file content."""
        if self.file:
            with self.file.open() as file:
                return file.read().decode()
        else:
            return ''

    def pull_binary(self) -> typing.Optional[bytearray]:
        if self.file:
            return self.file.open('rb').read()
        return None

    def push(self, archive: typing.Union[str, typing.IO]):
        if isinstance(archive, str):
            f = ContentFile(archive.encode('utf-8'))
        else:
            f = File(archive)
        self.file.save(self.path, f)
        self.size = self.file.size


class GithubSource(Source):
    """A project hosted on Github."""

    provider_name = 'GitHub'
    type_id = 'github'

    repo = models.TextField(
        null=False,
        blank=False,
        help_text='The Github repository identifier i.e. org/repo'
    )

    subpath = models.TextField(
        null=True,
        blank=True,
        help_text='Path to file or folder within the repository'
    )

    def __str__(self) -> str:
        return '{}/{}'.format(self.repo, self.subpath or '')


class GitlabSource(Source):
    """A project hosted on Gitlab."""

    provider_name = 'GitLab'
    type_id = 'gitlab'

    class Meta:
        abstract = True


class GoogleDocsSource(Source):
    """A reference to a Google Docs document."""

    provider_name = 'GoogleDocs'
    type_id = 'googledocs'

    doc_id = models.TextField(
        null=False,
        help_text='Google\'s ID of the document.'
    )

    @property
    def mimetype(self) -> str:
        return 'application/vnd.google-apps.document'

    @property
    def description(self) -> str:
        return self.path.split('/')[-1]

    def to_json(self) -> dict:
        return {
            'type_id': self.type_id,
            'pk': self.pk,
            'doc_id': self.doc_id,
            'path': self.path
        }


class OSFSource(Source):
    """
    A project hosted on the Open Science Framework.

    See https://developer.osf.io/ for API documentation.
    """

    provider_name = 'OSF'
    type_id = 'osf'

    class Meta:
        abstract = True


class SourceType(typing.NamedTuple):
    """
    Identifying information for a Source Type.

    id: short unique identifier
    name: display name
    model: the Source subclass
    """

    id: str
    name: str
    model: typing.Type[Source]

    @classmethod
    def from_source_class(cls, source_class: typing.Type[Source]) -> "SourceType":
        return cls(source_class.type_id, source_class.provider_name, source_class)


class AvailableSourceType(enum.Enum):
    """Enum for each available SourceType. For two-way lookup name to values etc."""

    FILE = SourceType.from_source_class(FileSource)
    GITHUB = SourceType.from_source_class(GithubSource)
    GOOGLE_DOCS = SourceType.from_source_class(GoogleDocsSource)

    # _type_lookup type checking is ignored throughout because it must be added at runtime to the class but then mypy
    # doesn't understand this

    @classmethod
    def setup_model_lookup(cls) -> None:
        if not hasattr(cls, "_type_lookup"):
            cls._type_lookup = {  # type: ignore
                source_type.value.id: source_type.value for source_type in cls
            }

    @classmethod
    def model_lookup(cls, type_id: str):
        cls.setup_model_lookup()
        return cls._type_lookup[type_id].model  # type: ignore


class LinkedSourceAuthentication(object):
    """Container for token(s) a user has for authenticating to remote sources."""

    github_token: typing.Optional[str]
    google_token: SocialToken

    def __init__(self, github_token: typing.Optional[str] = None,
                 google_token: typing.Optional[SocialToken] = None) -> None:
        self.github_token = github_token
        self.google_token = google_token
