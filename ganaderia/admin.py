# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from ganaderia.models import Animal,Especie,FichaMedica,Genero,Vacuna
# Register your models here.

admin.site.register(Animal)
admin.site.register(Especie)
admin.site.register(FichaMedica)
admin.site.register(Genero)
admin.site.register(Vacuna)