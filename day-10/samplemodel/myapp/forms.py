from django.forms import ModelForm
from myapp.models import Student

class StudentForm(ModelForm):
	class Meta:
		model=Student
		fields='__all__'#[student......]