# accounts/forms.py
from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth import get_user_model

User = get_user_model()  # sempre use get_user_model(), nunca importe User diretamente


class CustomUserCreationForm(UserCreationForm):
    """Formulário de registro de novo usuário."""

    email = forms.EmailField(required=True)

    class Meta(UserCreationForm.Meta):
        model = User
        fields = ('username', 'email', 'password1', 'password2')

    def clean_email(self):
        """Valida que o email não está em uso."""
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError('Este email já está em uso.')
        return email


class CustomUserChangeForm(UserChangeForm):
    """Formulário de edição de usuário (usado no admin)."""

    class Meta(UserChangeForm.Meta):
        model = User
        fields = ('username', 'email', 'bio', 'avatar')