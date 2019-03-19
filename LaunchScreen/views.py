from django.http import HttpResponse
from django.shortcuts import render


def initial_view(request):
    return render(request, 'LaunchScreen/main_screen.html')


def index(request):
    return render(request, 'LaunchScreen/main_screen.html')
