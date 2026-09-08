from django.urls import path
from . import views

app_name = 'appAndrea'

urlpatterns = [
    path('a1/', views.vistaAndrea, name = 'appAndreaa'),
]