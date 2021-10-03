from django.shortcuts import render

posts = [
    {
        'author': 'jack',
        'plant': 'calathea',
        'watered': 'yes',
        'date': '1st October 2021'
    },
    {
        'author': 'jack',
        'plant': 'rubber plant',
        'watered': 'no',
        'date': '1st October 2021'
    }
]


def home(request):
    context = {
        'posts': posts
    }
    return render(request, 'plants/home.html', context)


def about(request):
    return render(request, 'plants/about.html', {'title': 'About'})
