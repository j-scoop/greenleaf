from django.shortcuts import render
from.models import Plant


def home(request):
    context = {
        'plants': Plant.objects.all()
    }
    return render(request, 'plants/home.html', context)


def about(request):
    return render(request, 'plants/about.html', {'title': 'About'})
