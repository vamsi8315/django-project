from django.shortcuts import render
import random
from Emailsend import settings
from django.core.mail import send_mail
from django.http import HttpResponse
#from Emailsend.settings import EMAIL_HOST_USER
from Firstapp.models import Email

# Create your views here.
def email(request):
	if(request.method=='POST'):
		email=request.POST['email']
		subject=request.POST['subject']
		body=request.POST['body']
		sender=settings.EMAIL_HOST_USER
		reciever=email
		send_mail(subject,body,sender,[reciever])
		return HttpResponse("<h2>Please check your mail</h2>"+email)

	return render(request,'Firstapp/email.html')
def register(request):
	if request.method=='POST':
		fname=request.POST['fname']
		lname=request.POST['lname']
		uname=request.POST['username']
		email=request.POST['email']
		password=random.randint(100000,999999)
		Email.objects.create(first_name=fname,last_name=lname,email=email,user_name=uname,password=password)
		subject="Regardin your login details.."
		body="""
		Hello {}\n \n this is your Username:{} \n\n
		{} your password :\n\n
		""".format(fname,uname,password)
		sender=settings.EMAIL_HOST_USER
		reciever=email
		send_mail(subject,body,sender,[reciever])
		return HttpResponse("check your mail for otp")
	return render(request,'Firstapp/register.html')