from django.shortcuts import render, get_object_or_404, reverse
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Plant, PlantData
from .forms import PlantEntryForm


class PlantListView(ListView):
    """List plants on homepage"""
    model = Plant
    template_name = "plants/home.html"
    context_object_name = 'plants'
    ordering = ['-date_added']
    paginate_by = 10


class UserPlantListView(ListView):
    """List only the selected users plants"""
    model = Plant
    template_name = "plants/user_plants.html"
    context_object_name = 'plants'
    paginate_by = 10

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Plant.objects.filter(owner=user).order_by('-date_added')


class PlantDetailView(DetailView):
    """Show an individual plants attributes"""
    model = Plant
    template_name = "plants/plant_detail.html"
    context_object_name = 'plant'


class PlantCreateView(LoginRequiredMixin, CreateView):
    """Create a new plant object"""
    model = Plant
    # template_name = "plants/plant-form.html" ## Django automatically look for this filename
    fields = ['name', 'image']

    def form_valid(self, form):
        form.instance.owner = self.request.user  # set user as form author
        return super().form_valid(form)  # run the form


class PlantUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    """Update an existing plant object's attributes"""
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


class PlantEntryView(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    """Add plant data e.g. when watered, notes, and new photos"""
    template_name = 'plants/plant_entry_form.html'
    model = PlantData
    fields = ['date_watered', 'note']  #, 'photo']

    def get_success_url(self):
        return reverse('plant-detail', kwargs={'pk': self.kwargs.get('pk')})

    def form_valid(self, form):
        form.instance.plant = Plant.objects.get(id=self.kwargs.get('pk'))
        return super().form_valid(form)  # run the form

    def get_context_data(self, **kwargs):
        # Pass the plant object to the template
        context = super().get_context_data(**kwargs)
        context['plant'] = Plant.objects.get(pk=self.kwargs['pk'])
        return context

    def test_func(self):
        if self.request.user == Plant.objects.get(pk=self.kwargs['pk']).owner:
            return True
        return False


class PlantEntryDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    """Delete an existing plant object"""
    model = PlantData
    success_url = "/"  # Change to plant detail page

    def form_valid(self, form):
        form.instance.owner = self.request.user  # set user as form author
        return super().form_valid(form)  # run the form

    def test_func(self):
        plant = self.get_object()
        if self.request.user == plant.owner:
            return True
        return False


class PlantDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    """Delete an existing plant object"""
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
    """An about page"""
    return render(request, 'plants/about.html', {'title': 'About'})
