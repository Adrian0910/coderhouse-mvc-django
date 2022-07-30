
from django.contrib import admin
from django.urls import path

from familia_integrantes.views import list_familia, create_familiar

urlpatterns = [
    path('admin/', admin.site.urls),
    path('create/', create_familiar, name='create_familiar'),
    path('familiares/', list_familia, name='list_familiar')
]
