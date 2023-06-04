from django.db import models

class Employee(models.Model):
    first_name = models.CharField(max_length=100)
    middle_name = models.CharField(max_length=100, blank=True)
    last_name = models.CharField(max_length=100)
    address = models.CharField(max_length=200)
    email = models.EmailField()
    mobile = models.CharField(max_length=15)

    qualifications = models.ManyToManyField('Qualification', related_name='employees')

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class Qualification(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
