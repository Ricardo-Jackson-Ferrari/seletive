from django.urls import path

from . import views

app_name = 'empresa'

urlpatterns = [
    path('', views.listing, name='listagem'),
    path('nova_empresa/', views.register, name='registro'),
    path('excluir_empresa/<int:id>', views.delete, name='excluir'),
    path('<int:id>', views.detail, name='detalhe'),
]
