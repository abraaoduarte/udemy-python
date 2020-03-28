from django.urls import path, include, re_path
from courses import views

app_name = 'courses'

urlpatterns = [
    path('', views.index, name='index'),
    # path('/detalhes', views.index, name='details'),
    # re_path(r'^(?P<pk>\d+)/$', views.details, name='details'),
    path('<slug:slug>/', views.details, name='details'),
]