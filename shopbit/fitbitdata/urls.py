from django.urls import path

from . import views

urlpatterns = [
    path('', views.fitbit_login, name='fitbit_login'),
    path('home/', views.main_page, name='main_page'),
    path('badges/', views.view_badges, name='view_badges')
]