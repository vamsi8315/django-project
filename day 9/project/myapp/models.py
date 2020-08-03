from django.db import models

# Create your models here.
class Emp(models.Model):
	first_name=models.CharField(length=30,null=True)#length restriction for email or username id
	last_name=models.CharField(max_length=50)
	age=models.IntegerField(null=True)
	def __str__(self):
		return self.first_name+" "+self.last_name+" "+str(self.age)
class Emp1(models.Model):
	username=models.CharField(max_length=20,null=True)
	last_name=models.CharField(max_length=30)