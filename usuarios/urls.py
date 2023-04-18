from django.urls import path
from . import views

urlpatterns = [
    path('cadastro/', views.cadastro, name='cadastro'),  # pagina de cadastro
    path('login/', views.login, name='login'),  # pagina de login
    # pagina que apenas cadastrados tem acesso
    path('plataforma/', views.plataforma, name='plataforma')
]
