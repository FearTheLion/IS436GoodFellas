from django.http import HttpResponse, Http404
from django.shortcuts import render
import json

from .forms import *
from .models import *
from django.template.loader import render_to_string


def initial_view(request):
    interests_list = PrimaryInterest.objects.all()
    major_list = Major.objects.all()
    class_list = Course.objects.all()
    sample_form = ExampleInterestForm()
    context = {'interests_list': interests_list, 'major_list': major_list, 'class_list': class_list,
               'sample_form': sample_form}
    return render(request, 'LaunchScreen/main_screen.html', context)


def submit_initial_input(request):
    if request.method == 'POST':
        avg_salary = request.POST.get('avg_salary')
        if avg_salary == 'low':
            avg_salary = '30,000 - 50,000'
        elif avg_salary == 'med':
            avg_salary = '50,000 - 80,000'
        elif avg_salary == 'high':
            avg_salary = '80,000+'

        primary_interests = json.loads(request.POST.get('primary_interests'))
        search_primary_interests = []
        reset = PrimaryInterest.objects.all()
        for interest in reset:
            interest.checker = False
            interest.save()
        for key in primary_interests:
            value = PrimaryInterest.objects.get(pk=key['value'])
            value.checker = True
            print(value.checker)
            search_primary_interests.append(value)
            value.save()
        returned_majors_init = Major.objects.filter(avg_starting_salary=avg_salary)
        to_be_deleted = []
        for major in returned_majors_init:
            flag = True
            for p_i in search_primary_interests:
                for interest in major.related_primary_interest.all():
                    if interest.name == p_i.name:
                        flag = False
            if flag:
                to_be_deleted.append(major.id)
        returned_majors_init = returned_majors_init.exclude(id__in=to_be_deleted)
        returned_majors_init.order_by('tag_weight')
        context = {'msg': 'Success',
                   'out': render_to_string('LaunchScreen/major_list.html', {'major_list': returned_majors_init},
                                           request)}
        return render_to_json(request, context)
    return Http404()


def major_detail(request, m_id):
    class_list = Course.objects.filter(related_major=Major.objects.get(pk=m_id)).order_by('abbreviation')
    major = Major.objects.get(pk=m_id)
    context = {'class_list': class_list, 'major': major}
    return render(request, 'LaunchScreen/major_detail.html', context)


def gre_search(request):
    gre_search_form = GRESearchForm()
    return render(request, 'LaunchScreen/gre_search.html', context={'gre_search': gre_search_form})


def submit_gre_form(request):
    if request.method == 'POST':
        primary_interests = json.loads(request.POST.get('primary_interests'))
        search_primary_interests = []
        reset = PrimaryInterest.objects.all()
        for interest in reset:
            interest.checker = False
            interest.save()
        for key in primary_interests:
            value = PrimaryInterest.objects.get(pk=key['value'])
            value.checker = True
            search_primary_interests.append(value)
            value.save()
        returned_classes_init = Course.objects.filter(gre_class=True)
        to_be_deleted = []
        for course in returned_classes_init:
            flag = True
            for p_i in search_primary_interests:
                for interest in course.related_primary_interest.all():
                    if interest.name == p_i.name:
                        flag = False
            if flag:
                to_be_deleted.append(course.id)
        returned_classes = returned_classes_init.exclude(id__in=to_be_deleted)
        returned_classes.order_by('tag_weight')
        context = {'msg': 'Success',
                   'out': render_to_string('LaunchScreen/class_list.html', {'class_list': returned_classes},
                                           request)}
        return render_to_json(request, context)
    return Http404()
# helper methods
def render_to_json(request, data):
    return HttpResponse(
        json.dumps(data, ensure_ascii=False),
    )
