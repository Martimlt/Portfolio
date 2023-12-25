from django.contrib import admin

# Register your models here.
from .models import Cadeira, Pessoa, Projeto, Competencia

admin.site.register(Cadeira)
admin.site.register(Pessoa)
admin.site.register(Projeto)
admin.site.register(Competencia)
