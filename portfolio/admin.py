from django.contrib import admin

# Register your models here.
from .models import Licenciatura, Pessoa, Projeto, Competencia, Contact, Mestrado

admin.site.register(Licenciatura)
admin.site.register(Pessoa)
admin.site.register(Projeto)
admin.site.register(Competencia)
admin.site.register(Contact)
admin.site.register(Mestrado)