from django.contrib import admin

from .models import (
    Account,
    AccountPermission,
    AccountRole,
    AccountUserRole,
    Team,
    ProductExtension,
)


@admin.register(Account)
class AccountAdmin(admin.ModelAdmin):
    pass


@admin.register(AccountPermission)
class AccountPermissionAdmin(admin.ModelAdmin):
    pass


@admin.register(AccountRole)
class AccountRoleAdmin(admin.ModelAdmin):
    pass


@admin.register(AccountUserRole)
class AccountUserRoleAdmin(admin.ModelAdmin):
    list_display = ["account", "user", "role"]


@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):
    pass


@admin.register(ProductExtension)
class ProductExtensionAdmin(admin.ModelAdmin):
    pass
