from django.db import models
import random
class StudentDetail(models.Model):
    sid = models.AutoField(primary_key=True)  # Assuming sid is an AutoField
    sno = models.IntegerField()
    sname = models.CharField(max_length=30)
    sclass = models.IntegerField()
    saddress = models.CharField(max_length=100)

class StudentMark(models.Model):
    roll = models.ForeignKey(StudentDetail, on_delete=models.CASCADE, related_name='student_marks')
    tamil = models.IntegerField()
    english = models.IntegerField()
    maths = models.IntegerField()
    science = models.IntegerField()
    socialscience = models.IntegerField()

class StudDetail(models.Model):
    sid = models.AutoField(primary_key=True)  # Assuming sid is an AutoField
    roll = models.IntegerField()
    sname = models.CharField(max_length=30)
    sclass = models.IntegerField()
    saddress = models.CharField(max_length=100)
    tamil = models.IntegerField()
    english = models.IntegerField()
    maths = models.IntegerField()
    science = models.IntegerField()
    socialscience = models.IntegerField()