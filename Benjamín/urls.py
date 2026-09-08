from django.urls import path
from . import views

app_name = 'Benjamín'

urlpatterns = [
    path('v1/', views.v1, name='Benjamínv1'),
    path('v2/', views.v2, name='Benjamínv2'),
]