from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect

#  Call Forms method from model_operations app
from model_operations.forms import ToppingForm

#  Call Model from model_operations app
from model_operations.models import Pizza, Topping

def manytomany(request):
    if request.method == 'POST':
        form = ToppingForm(request.POST)
        if form.is_valid():
            pizza_name = request.POST.get('pizza')
            toppings_inst , created= Topping.objects.get_or_create(name=request.POST.get('topping'))
            pizza = Pizza(name=pizza_name,toppings_id=toppings_inst.id)
            pizza.save()
    else:
        form = ToppingForm()
    return render(request, 'model_operations/manytomany.html')
