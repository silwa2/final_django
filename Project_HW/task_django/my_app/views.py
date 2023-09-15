from django.shortcuts import render


def index(request):
    return render(request, 'my_app/about.html')


def about(request):
    return render(request, 'my_app/index.html')
