from django.http import HttpResponse
from django.shortcuts import render

from .forms import *
from .models import *


def initial_view(request):
    interests_list = primaryInterests.objects.all()
    secondary_interests_list = secondaryInterests.objects.all()
    major_list = Major.objects.all()
    class_list =Uni_Class.objects.all()
    sample_form = ExampleInterestForm()
    context = {'interests_list': interests_list, 'major_list': major_list, 'class_list': class_list, 'secondary_interests_list': secondary_interests_list, 'sample_form': sample_form}
    return render(request, 'LaunchScreen/main_screen.html', context)


