from django.shortcuts import render,redirect
from myapp1.forms import UserForm,Userlogin,Books,Myform
from django.http import HttpResponse
from BookBoom import settings
from myapp1.models import Registration,Mybooks
from django.core.mail import send_mail
import random
from BookBoom.settings import EMAIL_HOST_USER
from django.contrib.auth.decorators import login_required



# Create your views here.
"""def register(request):
	if request.method=="POST":
		name=request.POST['name']#vamsi
		phno=request.POST['phno']#9553618158
		email=request.POST['email']
		password="bookboom"+name+"!@#"
		username=name+phno[-5:]
		subject="registration of bookboom"
		body="Regarding your registration your username {} your password {}".format(username,password)
		#username=vamsi18158
		#password=bookboomvamsi!@#
		reciver=email
		sender=settings.EMAIL_HOST_USER
		send_mail(subject,body,sender,[reciver])
		Registration.objects.create(name=name,email=email,phno=phno,username=username,password=password)
		return redirect('login')
	form=UserForm()
	return render(request,'myapp1/register.html',{'form':form})"""
def register(request):
 if request.method=="POST":
  data=Myform(request.POST)
  if data.is_valid():
   data.save()
   return HttpResponse("Done....")
  else:
  	return HttpResponse("please check again")
 form=Myform()
 return render(request,'myapp1/register.html',{'form':form})

"""def login(request):
	if request.method=="POST":
		username=request.POST['username']
		password=request.POST['password']
		data=Registration.objects.filter(username=username,password=password)
		if  data:
				return render(request,'myapp1/home.html',{'data':data})
		else:  
			return HttpResponse("check once its wrong details")
	form=Userlogin()
	return render(request,'myapp1/login.html',{'form':form})"""#new changes

def home(request):

	return render(request,'myapp1/home.html')
def addbook(request):
	if request.POST:
		data=Books(request.POST,request.FILES)
		if data.is_valid():
			data.save()
			return HttpResponse("added succesfully")
	form=Books()
	return render(request,'myapp1/addbook.html',{'form':form})
@login_required
def showbooks(request):
 data=Mybooks.objects.all()
 return render(request,'myapp1/showbooks.html',{'data':data})
def about(request):
	return render(request,'myapp1/about.html')
def contact(request):
	return render(request,'myapp1/contact.html')