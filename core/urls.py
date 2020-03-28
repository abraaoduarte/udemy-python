from django.urls import path, include
from core import views

app_name = 'core'

urlpatterns = [
    path('', views.home, name='home'),
    path('contato/', views.contact, name='contact'),
]