from django.db import models

# Create your models here.

class Usuario(models.Model):
    nome            = models.CharField(max_length=45)
    email           = models.CharField(max_length=45)
    senha           = models.CharField(max_length=45)
    auth            = models.CharField(max_length=40)
    
    def __unicode__(self):
        return self.nome