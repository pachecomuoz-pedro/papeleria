from django.urls import path
from login.views import login_inicio, login_papeleria, logout_papeleria

urlpatterns = [
    path('', login_inicio, name='login'),
    path('entrar', login_papeleria, name='login_papeleria'),
    path('salir', logout_papeleria, name='logout_papeleria'),
]
