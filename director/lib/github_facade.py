import typing

from allauth.socialaccount.models import SocialAccount, SocialApp, SocialToken
from django.contrib.auth.models import User
from github import Github
from github.Repository import Repository


def user_github_token(user: User) -> typing.Optional[str]:
    social_app = SocialApp.objects.filter(provider='github').first()  # assume just one github App is set up

    if social_app is None:
        return None

    social_account = SocialAccount.objects.filter(provider='github', user=user).first()

    if social_account is None:
        return None

    token = SocialToken.objects.filter(app=social_app, account=social_account).first()

    if token is None:
        return None

    return token.token


class GitHubFacade(object):
    _github_connector: typing.Optional[Github] = None
    _repository: typing.Optional[Repository] = None

    def __init__(self, repository_path: str, access_token: typing.Optional[str] = None) -> None:
        self.repository_path = repository_path
        self.access_token = access_token

    @property
    def github_connector(self) -> Github:
        if self._github_connector is None:
            self._github_connector = Github(self.access_token)
        return self._github_connector

    @property
    def repository(self) -> Repository:
        if self._repository is None:
            self._repository = self.github_connector.get_repo(self.repository_path)
        return self._repository

    def list_directory(self, relative_path: str) -> typing.Iterable[typing.Tuple[str, bool]]:
        while relative_path.endswith('/'):
            relative_path = relative_path[:-1]

        contents = self.repository.get_contents(relative_path)
        for content in contents:
            yield content.name, content.type == 'dir'

    def get_file_content(self, relative_path: str) -> str:
        f = self.repository.get_contents(relative_path)
        return f.decoded_content.decode('utf8')

    def put_file_content(self, relative_path: str, content: str, commit_message: str) -> None:
        f = self.repository.get_contents(relative_path)
        self.repository.update_file(f.path, commit_message, content, f.sha)