from django import forms
from django.contrib import admin
from .models import *


class ExampleInterestForm(forms.Form):

    avg_starting_salary_choices = (
        ('low', '30,000 - 50,000'),
        ('med', '50,000 - 80,000'),
        ('high', '80,000+')
    )

    primary_interest_choices = (
        ('tech', 'Technology'),
        ('health', 'Healthcare'),
        ('art', 'Artistic Expression'),
        ('math', 'Mathematics'),
        ('science', 'Science'),
    )

    secondary_interest_choices = (
        ('exercise', 'Exercise'),
        ('travel', 'Travel'),
        ('manual', 'Hands-on'),
        ('crit_think', 'Critical Thinking'),
    )

    avg_starting_salary = forms.ChoiceField(choices=avg_starting_salary_choices, label='Average Starting Salary')
    primary_interest = forms.MultipleChoiceField(choices=primary_interest_choices, label='Primary Interests')
    secondary_interest = forms.MultipleChoiceField(choices=secondary_interest_choices, label='Secondary Interests')


class ClassForm(forms.ModelForm):
    class Meta:
        model = Uni_Class
        fields = [
            'related_major', 'class_name', 'description', 'credits_earned', 'abbreviation',
            'interest_1', 'interest_2']
        labels = {
            'related_major': 'Related Major', 'class_name': 'Class Name', 'description': 'Class Description',
            'credits_earned': 'Credit Value',
            'interest_1': 'Primary Interests', 'interest_2': 'Secondary Interests',
            'abbreviation': 'Class Code'
        }


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
