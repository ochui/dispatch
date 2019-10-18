from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from accounts.forms import CustomUserCreationForm, CustomUserChangeForm
from accounts.models import CustomUser


@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):

    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    fieldsets = UserAdmin.fieldsets + (
        ('KYC', {'fields': ('phone_number', 'city', 'state')}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        ('KYC', {'fields': ('phone_number', 'city', 'state')}),
    )
    list_display = ['username', 'email', 'phone_number',  'city', 'state']
    list_filter = ['city', 'state', 'is_active', 'is_staff']
    model = CustomUser