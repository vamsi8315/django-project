#from django.shortcuts import render
from django.shortcuts import render
from myapp.forms import StudentForm
# Create your views here.

def register(request):
	if request.method=="POST":
		form=StudentForm(request.POST)
		form.save()
		messages.success(request,"Your data saved successfully!!")
	form=StudentForm()
	return render(request,'myapp/register.html',{'form':form})


# Create your views here.
"""def register(request):
 if request.method=="POST":
  form=StudentForm(request.POST)
  form.save()
  messages.success(request,'your data is added successfully')
  #return HttpResponse('Done')
 form=StudentForm()
 return render(request,'myapp/register.html',{'form':form})"""