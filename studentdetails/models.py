from django.db import models

# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=225)
    email = models.EmailField(max_length=75)
    mobile = models.IntegerField()
    department = models.TextField()
    father_name = models.TextField()
    ssc_marks = models.IntegerField()
    inter_marks = models.IntegerField()
    roll_number = models.IntegerField()
    image = models.ImageField(upload_to='media/')

    def __str__(self):
        return self.name

class Staff(models.Model):
    name = models.TextField()
    email = models.EmailField(max_length=75)
    department = models.TextField()
    mobile = models.IntegerField()
    experience = models.IntegerField()
    qualification = models.TextField()
    image = models.ImageField(upload_to='media/')

    def __str__(self):
        return self.name
