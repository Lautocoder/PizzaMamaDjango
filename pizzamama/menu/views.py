from django.shortcuts import render
from django.http import HttpResponse
from .models import Pizza


# Create your views here.

#/menu
def index(request):
    """pizzas = Pizza.objects.all()
    pizzas_names_and_prices = [f"{pizza.nom} : {pizza.prix} $" for pizza in pizzas]
    pizzas_names_and_prices_str = ', '.join(pizzas_names_and_prices)
    return HttpResponse(f"Les pizzas : {pizzas_names_and_prices_str}")"""
    pizzas = Pizza.objects.all().order_by('prix')
    return render(request,'menu/index.html',{'pizzas': pizzas})
