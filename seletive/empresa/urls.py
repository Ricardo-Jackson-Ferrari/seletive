from django.urls import path

from . import views

app_name = 'empresa'

urlpatterns = [
    path('', views.listagem, name='listagem'),
    path('nova_empresa/', views.registro, name='registro'),
    path('excluir_empresa/<int:id>', views.excluir, name='excluir'),
    path('<int:id>', views.detalhe, name='detalhe'),
]
