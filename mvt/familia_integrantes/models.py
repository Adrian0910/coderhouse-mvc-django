from django.db import models

# Create your models here.
class Familia(models.Model):
    name = models.CharField(max_length=45)
    last_name = models.CharField(max_length=45, null=True)
    parentesco = models.CharField(max_length=45, null=True)
    edad = models.IntegerField()
    fecha_creacion = models.DateField(null=True, blank=True, auto_now_add=True)
    



