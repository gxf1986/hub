import typing

from django.contrib.auth import get_user_model
from django.contrib.auth.models import AbstractUser
from django.shortcuts import get_object_or_404

from accounts.db_facade import user_is_account_admin
from accounts.models import Team
from projects.permission_models import (
    ProjectRole,
    ProjectAgentRole,
    ProjectPermissionType,
    ProjectPermission,
)
from projects.project_models import Project

User = get_user_model()

READ_ONLY_PROJECT_ROLE_NAME = "Viewer"


class ProjectFetchResult(typing.NamedTuple):
    """
    Represents the result of fetching a project for a particular agent (`User` or `Team`).

    The properties it includes are:
    -- agent_roles: roles the current agent (`User`/`Team`) has for the `Project``
    -- agent_permissions: all permissions the current agent (`User`/`Team`) has for the `Account`, i.e. combined
        permissions of all roles
    """

    project: Project
    agent_roles: typing.Set[ProjectRole]
    agent_permissions: typing.Set[ProjectPermissionType]


def add_roles_to_permissions_sets(
    roles_set: typing.Set[ProjectRole],
    permissions_set: typing.Set[ProjectPermissionType],
    role: ProjectRole,
) -> None:
    if role not in roles_set:
        roles_set.add(role)
        for permission_type in role.permissions_types():
            permissions_set.add(permission_type)


def fetch_project_for_user(
    user: AbstractUser,
    project_pk: typing.Optional[typing.Union[str, int]] = None,
    account_name: typing.Optional[str] = None,
    project_name: typing.Optional[str] = None,
    project: typing.Optional[Project] = None,
) -> ProjectFetchResult:
    # A Project can be passed in to prevent fetching again
    if not project:
        if account_name or project_name:
            if not account_name or not project_name:
                # For some reason we only have one of these
                raise ValueError("Both account_name and project_name must be provided.")
            project = get_object_or_404(
                Project, account__name=account_name, name=project_name
            )
        elif project_pk:
            project = get_object_or_404(Project, pk=project_pk)

    if not project:
        raise ValueError(
            "Either pk or account_name and project_name or project must be provided."
        )

    roles: typing.Set[ProjectRole] = set()
    permissions: typing.Set[ProjectPermissionType] = set()

    if user.is_authenticated and user_is_account_admin(user, project.account):
        # If user is an admin of the account, they have ProjectPermissionType.OWN  (highest) permission
        own_permission = ProjectPermission.objects.get(
            type=ProjectPermissionType.OWN.value
        )
        for role in ProjectRole.objects.filter(permissions__in=[own_permission]):
            add_roles_to_permissions_sets(roles, permissions, role)
    else:
        user_teams = Team.objects.filter(members=user) if user.is_authenticated else []

        project_agent_roles = ProjectAgentRole.filter_with_user_teams(
            user, user_teams, project=project
        )

        if project_agent_roles.count():
            for project_agent_role in project_agent_roles:
                add_roles_to_permissions_sets(
                    roles, permissions, project_agent_role.role
                )
        elif project.public:
            read_only_role = ProjectRole.objects.get(name=READ_ONLY_PROJECT_ROLE_NAME)

            add_roles_to_permissions_sets(roles, permissions, read_only_role)

    return ProjectFetchResult(project, roles, permissions)
