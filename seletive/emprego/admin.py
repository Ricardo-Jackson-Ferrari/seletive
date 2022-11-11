from django.contrib import admin

from .models import Emails, Emprego, Tarefa

admin.site.register(Emprego)
admin.site.register(Tarefa)
admin.site.register(Emails)
