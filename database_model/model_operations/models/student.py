from django.db import models

class Project(models.Model):
    project_name = models.CharField(max_length=100)

    def __str__(self):
        return self.project_name

class Student(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=100)
    project_name = models.ForeignKey(Project, on_delete=models.CASCADE)

    def __str__(self):
        return self.first_name
