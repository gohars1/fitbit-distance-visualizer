from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from . import views

urlpatterns = [
   path('share/', views.share_badge, name='share_badge'),
   path('feed/', views.view_feed, name='view_feed'),
   path('delete/', views.delete_post, name='delete-post')
]