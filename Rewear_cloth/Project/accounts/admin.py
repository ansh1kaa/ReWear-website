from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import User
from django.utils.translation import gettext_lazy as _

class UserAdmin(BaseUserAdmin):
    model = User
    ordering = ['email']
    list_display = ('email', 'name', 'is_staff', 'is_seller', 'is_superuser')
    list_filter = ('is_staff', 'is_seller', 'is_superuser')

    fieldsets = (
        (None, {'fields': ('email', 'name', 'password')}),
        (_('Permissions'), {
            'fields': ('is_active', 'is_staff', 'is_seller', 'is_superuser', 'groups', 'user_permissions'),
        }),
        (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'name', 'password1', 'password2', 'is_staff', 'is_seller', 'is_superuser'),
        }),
    )

    search_fields = ('email', 'name')
    readonly_fields = ('last_login', 'date_joined')

admin.site.register(User, UserAdmin)

