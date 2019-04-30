from django import forms
from django.contrib import admin
from .models import *


class ExampleInterestForm(forms.Form):
    avg_starting_salary_choices = (
        ('low', '30,000 - 50,000'),
        ('med', '50,000 - 80,000'),
        ('high', '80,000+')
    )
    avg_starting_salary = forms.ChoiceField(choices=avg_starting_salary_choices, label='Average Starting Salary')
    primary_interest = forms.ModelMultipleChoiceField(queryset=PrimaryInterest.objects.all(), label='Interest')


class GRESearchForm(forms.Form):
    primary_interest = forms.ModelMultipleChoiceField(queryset=PrimaryInterest.objects.all(), label='Interest')

