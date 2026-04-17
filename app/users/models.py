from django.db import models

from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    # Campos que já existem no AbstractUser: username, first_name, last_name, email, password, last_login, is_superuser 
    # Campo Extra para o Kinote
    foto_url = models.URLField(max_length=500, blank=True, null=True)

    def __str__(self):
        return self.username
    