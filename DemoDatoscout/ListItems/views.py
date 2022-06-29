from django.shortcuts import render
from django.http import HttpResponse
from .models import Producto

# Create your views here.
def index(request):
    return render(request, 'ListItems/index.html')

def lista(request):
    lista = Producto.objects.all()
    data = {
        'producto': lista
    }
    return render(request, 'ListItems/list.html', data)