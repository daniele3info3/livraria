from django.contrib import admin

# Register your models here.
from core.models import Autor, Categoria, Editora

admin.site.register(Autor)
admin.site.register(Categoria)
admin.site.register(Editora)