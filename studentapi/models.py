from django.db import models

# Create your models here.
class Student(models.Model):
    fullname = models.CharField(max_length=100)
    student_id = models.CharField(max_length = 3)
    student_age = models.CharField(max_length=3)

#Create  -POST
#Retrieve -GET
#Update - PUT
#Delete / Remove- Delete