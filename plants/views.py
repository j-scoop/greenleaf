from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView
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


class PlantCreateView(CreateView):
    model = Plant
    # template_name = "plants/plant-form.html" ## Django automatically look for this filename
    fields = ['name', 'image']

    def form_valid(self, form):
        form.instance.owner = self.request.user  # set user as form author
        return super().form_valid(form)  # run the form


def about(request):
    return render(request, 'plants/about.html', {'title': 'About'})
