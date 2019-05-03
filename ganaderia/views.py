# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse
from ganaderia.models import Animal,Especie,FichaMedica,Genero,Vacuna,Producto
from ganaderia.forms import AnimalForm,FichaMedicaForm,EspecieForm,GeneroForms,VacunaForms,ProductoForm
from django.views.generic import ListView, UpdateView,CreateView,DeleteView, TemplateView,View
from django.core.urlresolvers import reverse_lazy
from django.contrib.auth.models import User
# import serial
from django.contrib.messages.views import SuccessMessageMixin
# PDF
# from AgrobitPruebaDos.pdf_creador import render_pdf


# Create your views here.

def index(request):
    return render(request,'ganaderia/index_ganaderia.html')

class FichaMedicaViews(CreateView):
	model = FichaMedica
	form_class = FichaMedicaForm
	template_name = 'ganaderia/ficha_medica.html'
	success_url = reverse_lazy('ganaderia:agregar_fm')

class ProductoViews(CreateView):
	model = Producto
	form_class = ProductoForm
	template_name = 'ganaderia/producto_add.html'
	success_url = reverse_lazy('ganaderia:listar_pro')

class ProductoList(ListView):
    model = Producto
    template_name = 'ganaderia/producto_list.html'
    paginate_by = 5	

class FichaMedicaList(ListView):
    model = FichaMedica
    template_name = 'ganaderia/ficha_listar.html'
    paginate_by = 5

class FichaMedicaUpdate(UpdateView):
	model = FichaMedica
	form_class = FichaMedicaForm
	template_name = 'ganaderia/ficha_medica.html'
	success_url = reverse_lazy('ganaderia:listar_fm')

class FichaMedicaDelete(DeleteView):
	model = FichaMedica
	template_name = 'eliminar_ficha.html'
	success_url = reverse_lazy('ganaderia:listar_fm')

# AMIKNAL

class AnimalCreate(CreateView):
	model = Animal
	form_class = AnimalForm	
	template_name = 'ganaderia/ani_agregar.html'
	success_url = reverse_lazy('ganaderia:listar_ani')
	

class AnimalList(ListView):
    model = Animal
    template_name = 'ganaderia/ani_listar.html'
    paginate_by = 5

class AnimalUpdate(UpdateView):
	model = Animal
	form_class = AnimalForm	
	template_name = 'ganaderia/ficha_medica.html'
	success_url = reverse_lazy('ganaderia:listar_fm')

class AnimalDelete(DeleteView):
	model = Animal
	template_name = 'eliminar_ficha.html'
	success_url = reverse_lazy('ganaderia:listar_fm')

# ESPECIE#############################################################################333
class EspecieViews(CreateView):
	model = Especie
	form_class = EspecieForm
	template_name = 'ganaderia/ficha_medica.html'
	success_url = reverse_lazy('ganaderia:agregar_fm')

class EspecieList(ListView):
    model = Especie
    template_name = 'ganaderia/ficha_listar.html'
    paginate_by = 5

class EspecieUpdate(UpdateView):
	model = Especie
	form_class = EspecieForm
	template_name = 'ganaderia/ficha_medica.html'
	success_url = reverse_lazy('ganaderia:listar_fm')

class EspecieDelete(DeleteView):
	model = Especie
	template_name = 'eliminar_ficha.html'
	success_url = reverse_lazy('ganaderia:listar_fm')
# GENERO#############################################################################333
class GeneroViews(CreateView):
	model = Genero
	form_class = GeneroForms
	template_name = 'ganaderia/ficha_medica.html'
	success_url = reverse_lazy('ganaderia:agregar_fm')

class GeneroList(ListView):
    model = Genero
    template_name = 'ganaderia/ficha_listar.html'
    paginate_by = 5

class GeneroUpdate(UpdateView):
	model = Genero
	form_class = GeneroForms
	template_name = 'ganaderia/ficha_medica.html'
	success_url = reverse_lazy('ganaderia:listar_fm')

class GeneroDelete(DeleteView):
	model = Genero
	template_name = 'eliminar_ficha.html'
	success_url = reverse_lazy('ganaderia:listar_fm')

# VACUNA#############################################################################333
class VacunaViews(CreateView):
	model = Vacuna
	form_class = VacunaForms
	template_name = 'ganaderia/ficha_medica.html'
	success_url = reverse_lazy('ganaderia:agregar_fm')

class VacunaList(ListView):
    model = Vacuna
    template_name = 'ganaderia/ficha_listar.html'
    paginate_by = 5

class VacunaUpdate(UpdateView):
	model = Vacuna
	form_class = VacunaForms
	template_name = 'ganaderia/ficha_medica.html'
	success_url = reverse_lazy('ganaderia:listar_fm')

class VacunaDelete(DeleteView):
	model = Vacuna
	template_name = 'eliminar_ficha.html'
	success_url = reverse_lazy('ganaderia:listar_fm')

# pdf metodos

# class PDFprueba(View):
# 	def get(self,request,*arg,**kwargs):
# 		mascota = FichaMedica.objects.all().order_by('id')
		
# 		contexto = {'mascotas':mascota,'user':request.user}
# 		pdf = render_pdf("pdf/pdf_archivo.html", contexto)			
# 		return HttpResponse(pdf, content_type = "application/pdf")

	

# def AgregarAnimales_1(request):
# 	model = Animal	
# 	PuertoSerie = serial.Serial('COM8', 9600)
# 		# Creamos un buble sin fin
# 	# template_name = 'ganaderia/animal_agregar.html'
# 	# while True:
# 	# leemos hasta que encontarmos el final de linea
# 	sArduino = PuertoSerie.readline()
# 	# Mostramos el valor leido y eliminamos el salto de linea del final
# 	print "Valor Arduino: " + sArduino.rstrip('\n')
# 	nfc = sArduino.rstrip
# 	# xdxd = {'model':model}
# 	contexto = {'nfc':nfc,'model':model}	
# 	return render(request, 'ganaderia/agregar_nfc.html',contexto)
#     # return { "form": form}
