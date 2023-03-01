from django.shortcuts import render


def index(request):
    return render(request, 'main/index.html')


def about(request):
    return render(request, 'main/about.html')


def post(request):
    return render(request, 'main/forma.html')


def get(request):
    return render(request, 'main/index.html')


def reg(request):
    return render(request, 'reg/index.html')

# Create your views here.
