from django.urls import path
from . import views

app_name = 'app0'

urlpatterns = [
    path('v1/', views.v1, name='app0v1'),

]