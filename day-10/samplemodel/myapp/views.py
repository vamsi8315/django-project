from django.shortcuts import render,redirect
from myapp.models import Emp
from django.http import HttpResponse
from myapp.forms import StudentForm
from myapp.models import Student
from django.contrib import messages
# Create your views here.
def store(request):
	if request.method=="POST":
		name=request.POST['name']
		coursename=request.POST['coursename']
		age=request.POST['age']
		Emp.objects.create(name=name,coursename=coursename,age=age)
	return render(request,'myapp/store.html')
def display(request):
	data=Emp.objects.all()
	return render(request,'myapp/display.html',{'info':data})
def delete(request,name):
	data=Emp.objects.all()
	data.delete()
	return HttpResponse(name+"deleted successfully..!!")# return redirect(/display) if we want string not to be printed
def update(request,age):
	data=Emp.objects.get(age=age)
	if request.method=="POST":
		name=request.POST['name']
		coursename=request.POST['coursename']
		age=request.POST['age']
		data.name=name
		data.coursename=coursename
		data.age=age
		data.save()
		return redirect('/display')


	return render(request,'myapp/update.html',{'data':data})
def register(request):
 if request.method=="POST":
  form=StudentForm(request.POST)
  form.save()
  messages.success(request,'your data is added successfully')
  #return HttpResponse('Done')
 form=StudentForm()
 return render(request,'myapp/register.html',{'form':form})
def details(request):
	data=Student.objects.all()
	return render(request,'myapp/details.html',{'data':data})
def edit(request,id):
 data=Student.objects.get(id=id)
 if request.method=="POST":
  form=StudentForm(request.POST,instance=data)
  if form.is_valid():
   form.save()
   return redirect('/details')
 form=StudentForm(instance=data)
 return render(request,'myapp/edit.html',{'form':form,'data':data})	

def delete(request,id):
 ob=Student.objects.get(id=id)
 if request.method=="POST":
  ob.delete()
  return redirect('/details')
 return render(request,'myapp/msg.html',{'info':ob})

