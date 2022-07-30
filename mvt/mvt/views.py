from django.http import HttpResponse
from django.shortcuts import render # mostrar html


def template(request):
    return render(request, 'template_familia.html', context={})


