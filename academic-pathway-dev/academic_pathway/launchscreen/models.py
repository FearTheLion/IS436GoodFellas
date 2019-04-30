from django.db import models


class PrimaryInterest(models.Model):
    name = models.CharField(max_length=200)
    checker = models.BooleanField(default=False)

    def __str__(self):
        return str(self.name)


class Major(models.Model):
    major_name = models.CharField(max_length=100)
    credits_req = models.IntegerField()
    avg_starting_salary_choices = (
        ('30,000 - 50,000', 'low'),
        ('50,000 - 80,000', 'med'),
        ('80,000+', 'high')
    )
    avg_starting_salary = models.CharField(choices=avg_starting_salary_choices, max_length=20, default='med')
    related_major = models.ForeignKey('self', on_delete=models.CASCADE, blank=True, null=True)
    related_primary_interest = models.ManyToManyField('PrimaryInterest')
    tag_weight = models.IntegerField(default=0)

    def __str__(self):
        return str(self.major_name)


class Course(models.Model):
    course_name = models.CharField(max_length=600)
    abbreviation = models.CharField(max_length=20)
    description = models.TextField()
    credits_earned = models.IntegerField()
    related_major = models.ForeignKey(Major, on_delete=models.CASCADE)
    related_primary_interest = models.ManyToManyField('PrimaryInterest')

    def __str__(self):
        return str(self.course_name)


