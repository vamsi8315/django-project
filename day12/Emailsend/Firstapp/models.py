from django.db import models

# Create your models here.
class Email(models.Model):
	first_name=models.CharField(max_length=30,null=True)
	last_name=models.CharField(max_length=15,null=True)
	email=models.EmailField(max_length=30,null=True)
	user_name=models.CharField(max_length=30,null=True)
	password=models.CharField(max_length=100,null=True)
