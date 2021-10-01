from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='plants-home'),
    path('about/', views.about, name='plants-about'),
]
