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
        fields = ('username', 'email')

# Tela de edição do usuário
class CustomUserUpdateForm(UserChangeForm):
    # Sobrescrevemos o campo password para que ele não apareça ou 
    # apareça apenas como o link de "trocar senha" nativo do Django
    password = None 

    class Meta:
        model = User
        # Selecionamos apenas o que o usuário pode mudar no Kinote
        fields = ('username', 'email')
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Estilização Tailwind para os campos
        # for field_name, field in self.fields.items():
        #     field.widget.attrs.update({
        #         'class': 'w-full bg-slate-700 border border-slate-600 text-white rounded-lg p-2.5 focus:ring-amber-500 focus:border-amber-500 mb-4',
        #         'placeholder': field.label
        #     })