from django.db import models

from django.db import models
from django.contrib.auth.models import AbstractBaseUser, Permission


class User(AbstractBaseUser):
    name = models.CharField(max_length=250, verbose_name='Nome')
    email = models.EmailField(unique=True)
    is_owner = models.BooleanField(default=True, verbose_name='Propietário')

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['email']

    class Meta:
        verbose_name = 'Usuário'
        verbose_name_plural = 'Usuários'

    def __str__(self) -> str:
        return self.email
