from django.db import models


# Create your models here.
class Selection_Form(models.Model):
    course_load = models.IntegerField()
    avg_starting_salary_choices = (
        ('30,000 - 50,000', 'low'),
        ('50,000 - 80,000', 'med'),
        ('80,000+', 'high')
    )
    avg_starting_salary = models.CharField(choices=avg_starting_salary_choices, max_length=20)

    interest_1_choices = (
        ('Technology', 'tech'),
        ('Healthcare', 'health'),
        ('Artistic Expression', 'art'),
        ('Mathematics', 'math'),
        ('Science', 'science'),
    )
    interest_1 = models.CharField(choices=interest_1_choices, max_length=20)

    interest_2_choices = (
        ('Exercise', 'exercise'),
        ('Travel', 'travel'),
        ('Hands-on', 'manual'),
        ('Critical Thinking', 'crit_think'),
    )
    interest_2 = models.CharField(choices=interest_2_choices, max_length=20)


class Major(models.Model):
    major_name = models.CharField(max_length=20)
    credits_req = models.IntegerField()
    # avg_starting_salary = models.OneToOneField(Selection_Form, on_delete=models.CASCADE, to_field='avg_starting_salary', unique=True)
    related_major = models.ForeignKey('self', on_delete=models.CASCADE)
    # major_interest_tag = models.ForeignKey(Selection_Form, on_delete=models.CASCADE, to_field='interest_1')
    # minor_interest_tag = models.ForeignKey(Selection_Form, on_delete=models.CASCADE, to_field='interest_2')

class Class(models.Model):
    related_major = models.ForeignKey(Major, on_delete=models.CASCADE)
    class_name = models.CharField(max_length=20)
    abbreviation = models.CharField(max_length=20)
    description = models.TextField()
    credits_earned = models.IntegerField()
    # class_major_interest_tag = models.ForeignKey(Selection_Form, on_delete=models.CASCADE, to_field='interest_1')
    # class_minor_interest_tag = models.ForeignKey(Selection_Form, on_delete=models.CASCADE, to_field='interest_2')


