from django.shortcuts import render, redirect

def index(request):
    return render(request, 'model_operations/index.html')
