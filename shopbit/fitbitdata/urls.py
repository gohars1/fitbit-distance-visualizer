from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('home/<str:code>/<str:state>/', views.test_endpoint, name='test_endpoint')
]