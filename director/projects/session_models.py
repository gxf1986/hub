"""
Models implementing Stencila Hub Sessions.

Whenever a user is accessing a project and running the code in the interactive cells, Stencila Hub creates a Session which connects
to a Stencila Cloud instance which provides the environment for running the code. Each Session has parameters related to computational
resources.

Each Project can have a number of Sessions related to it. These Sessions are grouped in a Session Group.
"""

import enum

from django.db import models
from django.urls import reverse
from django.utils import timezone


class SessionStatus(enum.Enum):
    UNKNOWN = 'Unknown'
    NOT_STARTED = 'Not Started'
    RUNNING = 'Running'
    STOPPED = 'Stopped'


class Session(models.Model):
    """
    An execution Session
    """
    project = models.ForeignKey(
        'Project',
        null=False,
        on_delete=models.PROTECT,  # Don't want to delete references if the container is running and we need control still
        related_name='sessions',
        help_text='The Project that this Session belongs to.'
    )

    url = models.URLField(
        help_text='URL for API access to administrate this Session'
    )

    started = models.DateTimeField(
        null=True,
        help_text='DateTime this Session was started.'
    )

    stopped = models.DateTimeField(
        null=True,
        help_text='DateTime this Session was stopped (or that we detected it had stopped).'
    )

    last_check = models.DateTimeField(
        null=True,
        help_text='The last time the status of this Session was checked'
    )

    @property
    def status(self) -> SessionStatus:
        if self.last_check is None:
            return SessionStatus.UNKNOWN

        if self.stopped is not None and self.stopped <= timezone.now():
            return SessionStatus.STOPPED

        if self.started is not None and self.started <= timezone.now():
            return SessionStatus.RUNNING

        return SessionStatus.NOT_STARTED


class SessionParameters(models.Model):
    """
    Defines the parameters for new Sessions created in a Project
    """

    name = models.TextField(
        null=True,
        blank=True
        help_text='Names for the set of session parameters (optional). This can be used if you want to save a pre-set Session Parameters'
    )

    description = models.TextField(
        null=True,
        blank=True,
        help_text='Optional long description about the SessionParameters'
    )

    memory = models.FloatField(
        default=1,
        null=True,
        blank=True,
        help_text='Gigabytes (GB) of memory allocated'
    )

    cpu = models.FloatField(
        default=1,
        null=True,
        blank=True,
        help_text='CPU shares (out of 100 per CPU) allocated'
    )

    network = models.FloatField(
        null=True,
        blank=True,
        help_text='Gigabytes (GB) of network transfer allocated. null = unlimited'
    )

    lifetime = models.IntegerField(
        null=True,
        blank=True,
        help_text='Minutes before the session is terminated. null = unlimited'
    )

    timeout = models.IntegerField(
        default=60,
        null=True,
        blank=True,
        help_text='Minutes of inactivity before the session is terminated'
    )

    def __str__(self) -> str:
        return self.name if self.name else 'SessionParameters #{}'.format(self.id)

    def get_absolute_url(self):
        return reverse('sessionparameters_update', args=[self.pk])

    def serialize(self) -> dict:
        return {
            "pk": self.pk,
            "name": self.name,
            "description": self.description,
            "memory": self.memory,
            "cpu": self.cpu,
            "network": self.network,
            "lifetime": self.lifetime,
            "timeout": self.timeout
        }
