from django.urls import path
from . import views

app_name = 'app2'

urlpatterns = [
    path('v1/', views.v1, name='app2v1'),
    path('v2/', views.v2, name='app2v2'),
]