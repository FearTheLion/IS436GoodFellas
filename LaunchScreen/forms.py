from django import forms
from LaunchScreen.models import *


class ClassForm(forms.ModelForm):
    class Meta:
        model = Uni_Class
        fields = [
            'related_major', 'class_name', 'description', 'credits_earned',
            'class_major_interest_tag', 'class_minor_interest_tag', 'class_minor_interest_tag', 'class_code']
        labels = {
            'related_major': 'Related Major', 'class_name': 'Class Name', 'description': 'Class Description',
            'credits_earned': "Credit Value",
            'class_major_interest_tag': "Primary Interests", 'class_minor_interest_tag': "Secondary Interests",
            'class_code': "Class Code"
        }
        fields = [
            'class_name', 'class_code', 'description', 'related_major', 'credits_earned',
            'class_major_interest_tag', 'class_minor_interest_tag'
        ]

# class InterestForm(forms.ModelForm):
#     class Meta:
#         model = Interests
#         fields = [
#             'avg_starting_salary_choices', 'avg_starting_salary']
#             # 'interest_1_choices', 'interest_1',
#             # 'interest_2_choices', 'interest_2']
#         labels = {
#             'avg_starting_salary_choices': 'Average Starting Salary Ranges', 'avg_starting_salary': 'Average Starting Salary']
#             # 'interest_1_choices': 'Choices of primary interests',
#             # 'interest_2_choices': "Choices of secondary interests", 'interest_2': "Secondary Interests"}
#         fields = [
#             'avg_starting_salary_choices', 'avg_starting_salary',
#             # 'interest_1_choices', 'interest_2_choices', 'interest_2',
#         ]
