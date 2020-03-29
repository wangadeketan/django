from django.forms import ModelForm
from model_operations.models import Topping, Pizza

class PizzaForm(ModelForm):
    class Meta:
        model = Pizza
        fields = ['name','toppings']

class ToppingForm(ModelForm):
    class Meta:
        model = Topping
        fields = ['name']
