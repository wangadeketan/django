from django.contrib import admin

# Register your models here.
from model_operations.models import Project, Student

class StudentAdmin(admin.ModelAdmin):
    list_display = ('first_name','last_name','project_name')

admin.site.register(Student,StudentAdmin)
admin.site.register(Project)
