from django import forms
from django.contrib import admin
from .models import *


class ClassForm(forms.ModelForm):
    class Meta:
        model = Uni_Class
        fields = [
            'related_major', 'class_name', 'description', 'credits_earned',
            'class_major_interest_tag', 'class_minor_interest_tag', 'class_minor_interest_tag', 'class_code']
        labels = {
            'related_major': 'Related Major', 'class_name': 'Class Name', 'description': 'Class Description',
            'credits_earned': 'Credit Value',
            'class_major_interest_tag': 'Primary Interests', 'class_minor_interest_tag': 'Secondary Interests',
            'class_code': 'Class Code'
        }
        fields = [
            'class_name', 'class_code', 'description', 'related_major', 'credits_earned',
            'class_major_interest_tag', 'class_minor_interest_tag'
        ]


class ClassFormAdmin(admin.ModelAdmin):
    form = ClassForm


class PrimaryInterestForm(forms.ModelForm):
    class Meta:
        model = primaryInterests
        fields = ['avg_starting_salary', 'course_load', 'interest_1']

        labels = {
            'avg_starting_salary_choices': 'Average Starting Salary Ranges', 'course_load': 'Course Load', 'interest_1': 'Primary Interest'
        }


class PrimaryInterestFormAdmin(admin.ModelAdmin):
    form = PrimaryInterestForm
