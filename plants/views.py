from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
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


class PlantCreateView(LoginRequiredMixin, CreateView):
    model = Plant
    # template_name = "plants/plant-form.html" ## Django automatically look for this filename
    fields = ['name', 'image']

    def form_valid(self, form):
        form.instance.owner = self.request.user  # set user as form author
        return super().form_valid(form)  # run the form


class PlantUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Plant
    # template_name = "plants/plant-form.html" ## Django automatically look for this filename
    fields = ['name', 'image']

    def form_valid(self, form):
        form.instance.owner = self.request.user  # set user as form author
        return super().form_valid(form)  # run the form

    def test_func(self):
        plant = self.get_object()
        if self.request.user == plant.owner:
            return True
        return False


class PlantDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Plant
    success_url = "/"

    def form_valid(self, form):
        form.instance.owner = self.request.user  # set user as form author
        return super().form_valid(form)  # run the form

    def test_func(self):
        plant = self.get_object()
        if self.request.user == plant.owner:
            return True
        return False


def about(request):
    return render(request, 'plants/about.html', {'title': 'About'})
