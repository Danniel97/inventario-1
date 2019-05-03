# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

class Vacuna(models.Model):
    nombre = models.CharField(max_length = 100)
	
    def __str__(self):
		return '{}'.format(self.nombre)

class Especie(models.Model):
    nombre = models.CharField(max_length = 100)

    def __str__(self):
		return '{}'.format(self.nombre)

class Genero(models.Model):
    nombre = models.CharField(max_length = 100)

    def __str__(self):
		return '{}'.format(self.nombre)


class Animal(models.Model):
    diio = models.IntegerField(null=True)   
    especies = models.ForeignKey(Especie, on_delete=models.CASCADE)

    def __str__(self):
		return '{}'.format(self.diio)

class FichaMedica(models.Model):
    codigo = models.IntegerField(null=False)
    descripcion = models.TextField(max_length=255)
    peso = models.IntegerField(null=False)    
    animal = models.ForeignKey(Animal, on_delete=models.CASCADE)
    genero = models.ForeignKey(Genero, on_delete=models.CASCADE)
    vacuna = models.ForeignKey(Vacuna, on_delete=models.CASCADE)
	
    def __str__(self):
		return '{}'.format(self.codigo)

class Producto(models.Model):
    codigo = models.IntegerField(null=False)
    descripcion = models.TextField(max_length=255)
    peso = models.IntegerField(null=False)    
    cantidad = models.IntegerField(null=False)
    
   # vacuna = models.ForeignKey(Vacuna, on_delete=models.CASCADE)
	
    def __str__(self):
		return '{}'.format(self.codigo)





