from django.db import models 
from accounts.models import User # Relação da minha models de Usuários da app accounts



class Entreprise(models.Model):
    name = models.CharField(max_length=200, verbose_name='Nome da Empresa')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    