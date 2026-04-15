from django.db import models
from django.utils import timezone
import datetime

from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    """
    Model de usuário customizado.
    Sempre use get_user_model() ou settings.AUTH_USER_MODEL
    para referenciar este model em outros lugares do projeto.
    """
    # Campos que já existem no AbstractUser: username, first_name, last_name, email, password, last_login, is_superuser 
    # Campo Extra para o Kinote
    foto_url = models.URLField(max_length=500, blank=True, null=True)

    def __str__(self):
        return self.username
    