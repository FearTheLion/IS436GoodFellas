from django.db import models


# Create your models here.
class primaryInterests(models.Model):
    course_load = models.IntegerField()
    avg_starting_salary_choices = (
        ('30,000 - 50,000', 'low'),
        ('50,000 - 80,000', 'med'),
        ('80,000+', 'high')
    )
    avg_starting_salary = models.CharField(choices=avg_starting_salary_choices, max_length=20, default='med')

    interest_1_choices = (
        ('Technology', 'tech'),
        ('Healthcare', 'health'),
        ('Artistic Expression', 'art'),
        ('Mathematics', 'math'),
        ('Science', 'science'),
    )
    interest_1 = models.CharField(choices=interest_1_choices, max_length=20)

    def __str__(self):
        return 'Course Load: ' + str(self.course_load) + ', Avg. Starting Salary: ' + str(self.avg_starting_salary) + ', Interest: ' + str(self.interest_1)


class secondaryInterests(models.Model):
    interest_2_choices = (
        ('Exercise', 'exercise'),
        ('Travel', 'travel'),
        ('Hands-on', 'manual'),
        ('Critical Thinking', 'crit_think'),
    )
    interest_2 = models.CharField(choices=interest_2_choices, max_length=20)

    def __str__(self):
        return str(self.interest_2)


class Major(models.Model):
    major_name = models.CharField(max_length=20)
    credits_req = models.IntegerField()
    related_major = models.ForeignKey('self', on_delete=models.CASCADE, blank=True, null=True)
    major_major_interest_tag = models.ForeignKey(primaryInterests, on_delete=models.CASCADE, related_name='major_major_interest_tag', null=True)
    major_minor_interest_tag = models.ForeignKey(secondaryInterests, on_delete=models.CASCADE, related_name='major_minor_interest_tag', null=True)

    def __str__(self):
        return str(self.major_name)


# noinspection PyPep8Naming
class Uni_Class(models.Model):
    related_major = models.ForeignKey(Major, on_delete=models.CASCADE)
    class_name = models.CharField(max_length=600)
    abbreviation = models.CharField(max_length=20)
    description = models.TextField()
    credits_earned = models.IntegerField()
    class_major_interest_tag = models.ForeignKey(primaryInterests, on_delete=models.CASCADE, related_name='class_major_interest_tag', null=True)
    class_minor_interest_tag = models.ForeignKey(secondaryInterests, on_delete=models.CASCADE, related_name='class_minor_interest_tag', null=True)

    def __str__(self):
        return str(self.class_name)


