from django.urls import path
from . import views

app_name = 'appemmanuel'

urlpatterns = [
    path('vista1/', views.vista1_appemmanuel, name='vista1_appemmanuel'),
]   