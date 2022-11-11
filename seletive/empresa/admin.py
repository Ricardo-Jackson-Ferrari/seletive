from django.contrib import admin

from .models import Empresa, NichoMercado, Tecnologia

admin.site.register(Empresa)
admin.site.register(NichoMercado)
admin.site.register(Tecnologia)
