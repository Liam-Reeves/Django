from django.db import models

# Create your models here.

class Student(models.Model):
    name = models.CharField(max_length=50)
    number = models.IntegerField()
    location =models.CharField(max_length=40)

    def __str__(self):
        return self.name

class Teacher(models.Model):
    name = models.CharField(max_length=50)
    number = models.IntegerField()
    location = models.CharField(max_length=40)
    subject = models.CharField(max_length=40)

    def __str__(self):
        return self.name

class Course(models.Model):
    name = models.CharField(max_length=50)
    duration = models.IntegerField()
    cost = models.IntegerField()
    def __str__(self):
        return self.name

class Assignment(models.Model):
    book = models.CharField(max_length=50)
    pages = models.IntegerField()
    duration = models.IntegerField()