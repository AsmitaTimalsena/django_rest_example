from django.db import models

# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=200)
    subject = models.CharField(max_length=200)
    enrollment_date = models.DateTimeField(auto_now_add=True)