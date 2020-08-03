from django.db import models

# Create your models here.
class Emp(models.Model):
	name=models.CharField(max_length=50,null=True)
	coursename=models.CharField(max_length=50)
	age=models.IntegerField(null=True)
	def __str__(self):
		return self.name
class Student(models.Model):
	branches=[('CSE','cse'),('ECE','ece'),('MECH','mech'),('IT','it')]
	stuid=models.CharField(max_length=10)
	stuName=models.CharField(max_length=50)
	branch=models.CharField(max_length=50,choices=branches)
	age=models.IntegerField()
	def __str__(self):
		return self.stuid+" "+self.stuName