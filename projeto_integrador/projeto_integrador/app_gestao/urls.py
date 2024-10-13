from django.urls import path
from . import views

urlpatterns = [
    # Adicione suas rotas aqui, por exemplo:
    path('', views.coleta_dados_usuario, name='cadastro.html'),
    path('cadastro/', views.cadastro, name='cadastro'),
     
]
