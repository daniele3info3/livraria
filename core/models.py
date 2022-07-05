from django.db import models

# Create your models here.
class Categoria(models.Model):
    descricao = models.CharField(max_length=255)

    def __str__(self):
        return self.descricao


# return self.descricao.upper()
