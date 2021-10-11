from django.shortcuts import render
from django.views.generic import ListView, DetailView
from.models import Plant


class PlantListView(ListView):
    model = Plant
    template_name = "plants/home.html"
    context_object_name = 'plants'
    ordering = ['-date_added']


class PlantDetailView(DetailView):
    model = Plant
    template_name = "plants/plant-detail.html"
    context_object_name = 'plant'


def about(request):
    return render(request, 'plants/about.html', {'title': 'About'})
