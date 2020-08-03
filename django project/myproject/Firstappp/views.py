from django.shortcuts import render
from Firstappp.models import Emp
from django.http import HttpResponse

def home(request):
	return render(request,'Firstappp/home.html')
# Create your views here.
# Create your views here.
def store(request):
 if request.method=="POST":
  first_name=request.POST['first_name']
  last_name=request.POST['last_name']
  age=request.POST['age']
  Emp.objects.create(first_name=first_name,last_name=last_name,age=int(age))
  #print(name,age,salary,desig,phno)

 return render(request,'Firstappp/store.html')