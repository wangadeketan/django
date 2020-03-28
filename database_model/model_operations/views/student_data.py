from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect

#  Call Forms method from model_operations app
from model_operations.forms import ProjectForm

#  Call Model from model_operations app
from model_operations.models import Project, Student

def save_student_data(request):
    if request.method == 'POST':
        student_form = ProjectForm(request.POST)
        if student_form.is_valid():
            first_name = request.POST.get('first_name')
            last_name = request.POST.get('last_name')
            project_name, created = Project.objects.get_or_create(project_name=request.POST.get('project_name'))
            student = Student(first_name=first_name,last_name=last_name,project_name_id=project_name.id)
            student.save()
            return HttpResponseRedirect("sucess")
    else:
        student_form = ProjectForm()
    return render(request, 'model_operations/index.html')
