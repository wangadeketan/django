from django.forms import ModelForm
from model_operations.models import Student, Project

class ProjectForm(ModelForm):
    class Meta:
        model = Project
        fields = ['project_name']

class StudentForm(ModelForm):
    class Meta:
        model = Student
        fields = ['first_name','last_name','project_name']
