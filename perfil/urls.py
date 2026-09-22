from django.urls import path
from . import views

app_name = 'perfil'

urlpatterns = [
    path('v1/', views.p1, name='perfilv1'),
    path('v2/', views.p2, name='perfilv2'),
]