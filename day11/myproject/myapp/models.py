from django.db import models


class Student(models.Model):
	branches=[('CSE','cse'),('ECE','ece'),('MECH','mech'),('IT','it')]
	stuid=models.CharField(max_length=10)
	stuName=models.CharField(max_length=50)
	branch=models.CharField(max_length=50,choices=branches)
	age=models.IntegerField()
	def __str__(self):
		return self.stuid+" "+self.stuName
# Create your models here.
