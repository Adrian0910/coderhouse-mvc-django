
from django.shortcuts import render
from familia_integrantes.models import Familia
# Create your views here.

def create_familiar(request):
    familiar = Familia.objects.create(name= 'Tanis', last_name='Santander', edad=54, parentesco='Padre')
    
    context = {
        'familiar': familiar,
    }
    return render(request, 'create_familiar.html', context=context)

def list_familia(request):
    familiares = Familia.objects.all()
    context = {
        'familiares': familiares
    }
    return render(request, 'familia.html', context=context)