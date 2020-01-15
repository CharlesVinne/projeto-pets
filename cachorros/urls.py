from django.urls import path
from cachorros.views import cadastro

urlpatterns = [
    path('cadastro/', cadastro),
]