from django.urls import path

from . import views

app_name = 'emprego'

urlpatterns = [
    path('registro/', views.registro, name='registro'),
    path('<int:id>', views.detalhe, name='detalhe'),
    path(
        'registro_tarefa/<int:id_vaga>',
        views.registro_tarefa,
        name='registro_tarefa',
    ),
    path(
        'realiza_tarefa/<int:id_tarefa>',
        views.realiza_tarefa,
        name='realiza_tarefa',
    ),
    path(
        'envia_email/<int:id_emprego>', views.envia_email, name='envia_email'
    ),
]
