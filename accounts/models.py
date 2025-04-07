from django.db import models
from django.contrib.auth.models import AbstractBaseUser, Permission
from companies.models import Entreprise

class User(AbstractBaseUser):
    name = models.CharField(max_length=250, verbose_name='Nome')
    email = models.EmailField(unique=True)
    is_owner = models.BooleanField(default=True, verbose_name='Propietário')

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['email']

    class Meta:
        verbose_name = 'Usuário'
        verbose_name_plural = 'Usuários'
        db_table = 'Usuarios'

    def __str__(self) -> str:
        return self.email
    

class Group(models.Model):
    name = models.CharField(max_length=90, verbose_name='Nome do Grupo')
    enterprise = models.ForeignKey(Entreprise, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Grupo'
        verbose_name_plural = 'Grupos'
        db_table = 'Grupo'

    def __str__(self) -> str:
        return self.name


class Group_Permissions(models.Model):
    group = models.ForeignKey(Group, on_delete=models.CASCADE)
    permissions = models.ForeignKey(Permission, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Grupo Permissão'
        verbose_name_plural = 'Grupos Permissões'
        db_table = 'Grupo Permissão'

    def __str__(self) -> str:
        return self.group

class UserGroups(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    group_user = models.ForeignKey(Group, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Grupo do Usuário'
        verbose_name_plural = 'Grupos dos Usuários'
        db_table = 'Grupo do Usuário'


    def __str__(self) -> str:
        return self.user
