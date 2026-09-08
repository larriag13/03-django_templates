from django.urls import path
from . import views

app_name = 'appOmar'

urlpatterns = [
    path('cv/', views.cv, name='appOmarcv'),
]