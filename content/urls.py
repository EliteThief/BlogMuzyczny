from django.urls import path
from . import views


urlpatterns = [
    path('', views.contentDataBase, name='content_db'),
]