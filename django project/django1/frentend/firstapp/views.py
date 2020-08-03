from django.shortcuts import render
def register(request):
	return render(request,'firstapp/register.html')
def table(request):
	return render(request,'firstapp/table.html')
# Create your views here.
