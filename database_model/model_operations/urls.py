from django.urls import path
from model_operations.views import index, save_student_data, manytomany

urlpatterns = [
     path('', index, name='index'),
     path('submit/', save_student_data , name='submit'),
     path('many/', manytomany , name='many'),
     ]
