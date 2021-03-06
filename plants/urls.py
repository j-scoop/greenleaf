from django.urls import path
from .views import (
    PlantListView, PlantDetailView, PlantCreateView, PlantUpdateView, PlantDeleteView, UserPlantListView,
    PlantEntryView, PlantEntryDeleteView
)
from . import views


urlpatterns = [
    path('', PlantListView.as_view(), name='plants-home'),
    path('about/', views.about, name='plants-about'),
    path('plant/<int:pk>/', PlantDetailView.as_view(), name='plant-detail'),
    path('plant/new/', PlantCreateView.as_view(), name='plant-create'),
    path('plant/<int:pk>/update/', PlantUpdateView.as_view(), name='plant-update'),
    path('plant/<int:pk>/delete/', PlantDeleteView.as_view(), name='plant-delete'),
    path('user/<str:username>/', UserPlantListView.as_view(), name='user-plants'),
    path('plant/<int:pk>/plant-entry/', PlantEntryView.as_view(), name='plant-entry'),
]
