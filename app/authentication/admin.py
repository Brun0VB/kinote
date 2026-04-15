# accounts/admin.py
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth import get_user_model

from .forms import CustomUserCreationForm, CustomUserChangeForm

User = get_user_model()


@admin.register(User)
class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = User

    # Colunas exibidas na listagem
    list_display = ('username', 'email', 'is_staff', 'is_active')
    list_filter = ('is_staff', 'is_active')
    search_fields = ('username', 'email')

    # Campos exibidos na página de edição
    fieldsets = UserAdmin.fieldsets + (
        ('Dados extras', {'fields': ('bio', 'avatar')}),
    ) # type: ignore

    # Campos exibidos na página de criação
    add_fieldsets = UserAdmin.add_fieldsets + (
        ('Dados extras', {'fields': ('email', 'bio')}),
    )