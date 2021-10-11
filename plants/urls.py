from django.urls import path
from .views import PlantListView, PlantDetailView
from . import views


urlpatterns = [
    path('', PlantListView.as_view(), name='plants-home'),
    path('about/', views.about, name='plants-about'),
    path('plant/<int:pk>/', PlantDetailView.as_view(), name='plant-detail'),
]
