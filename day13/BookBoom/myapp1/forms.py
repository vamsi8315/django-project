from django.forms import ModelForm
from myapp1.models import Registration,Mybooks 
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class Myform(UserCreationForm):
	class Meta:
		model=User
		fields=['username','first_name','last_name','password1','password2','email']
class UserForm(ModelForm):
	class Meta:
		model=Registration
		fields=['name','email','phno']#'__all__'
class Userlogin(ModelForm):
	class Meta:
		model=Registration
		fields=['username','password']
class Books(ModelForm):
 class Meta:
  model=Mybooks
  fields='__all__'
