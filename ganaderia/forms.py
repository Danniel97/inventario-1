from django import forms
from ganaderia.models import Animal,Especie,FichaMedica,Genero,Vacuna,Producto


class DateInput(forms.DateInput):
    input_type = 'date'
    
class AnimalForm(forms.ModelForm):
    class Meta:
        model = Animal
        fields = {'diio',
        'especies',}
        labels = {  
            'diio' : 'correlativo' ,             
            'especies':'Especie',    
        }
        widgets = {
            'diio':forms.NumberInput(attrs={'class': 'form-control'}) ,           
            'especies': forms.Select(attrs={'class': 'form-control-lg form-control'}),  
        }

class EspecieForm(forms.ModelForm):
    class Meta:
        model = Especie
        fields = {'nombre', }    
        labels = { 'nombre':'Nombre',}
        widgets = { 'nombre':forms.TextInput(attrs={'class': 'form-control'}) , }

class FichaMedicaForm(forms.ModelForm):
      class Meta:
        model=FichaMedica
        fields = [            
            'codigo',
            'descripcion',
            'peso',
            'animal',
            'genero',
            'vacuna',
        ]
        labels = {            
            'codigo':'Codigo',
            'descripcion':'Descripcion',
            'peso':'Peso',
            'animal':'Animal',
            'genero':'Genero',
            'vacuna':'Vacunas',           
        }
        widgets = {
            'codigo': forms.NumberInput(attrs={'class': 'form-control'}),
            'descripcion': forms.TextInput(attrs={'class': 'form-control'}),
            'peso': forms.NumberInput(attrs={'class': 'form-control'}),
            'animal': forms.SelectMultiple(attrs={'class': 'form-control'}),
            'genero': forms.SelectMultiple(attrs={'class': 'form-control'}),
            'vacuna': forms.SelectMultiple(attrs={'class': 'form-control'}),
        }



class ProductoForm(forms.ModelForm):
      class Meta:
        model=Producto
        fields = [            
            'codigo',
            'descripcion',
            'peso',
            'cantidad',
        ]
        labels = {            
            'codigo':'Codigo',
            'descripcion':'Descripcion',
            'peso':'Peso',
            'cantidad':'Cantidad',
                       
        }
        widgets = {
            'codigo': forms.NumberInput(attrs={'class': 'form-control'}),
            'descripcion': forms.TextInput(attrs={'class': 'form-control'}),
            'peso': forms.NumberInput(attrs={'class': 'form-control'}),
            'cantidad': forms.NumberInput(attrs={'class': 'form-control'}),
            
        }






class GeneroForms(forms.ModelForm):
      class Meta:
        model = Genero
        fields = {'nombre', }    
        labels = { 'nombre':'Nombre',}
        widgets = { 'nombre':forms.TextInput(attrs={'class': 'form-control'}) , }

class VacunaForms(forms.ModelForm):
      class Meta:
        model = Vacuna
        fields = {'nombre', }    
        labels = { 'nombre':'Nombre',}
        widgets = { 'nombre':forms.TextInput(attrs={'class': 'form-control'}) , }



# class AnimalForm(forms.ModelForm):
#     class Meta:
#         model = Animal
#         fields = {'diio',
#         'especie',}
#         labels = {  
#             'diio' : 'correlativo' ,             
#             'especie':'Especie',    
#         }
#         widgets = {
#             'diio':forms.TextInput(attrs={'class': 'form-control'}) ,           
#             'especie': forms.Select(),  
#         }
        # def AgregarAnimales_1(request):
        #     model = Animal	
        #     PuertoSerie = serial.Serial('COM8', 9600)
        #         # Creamos un buble sin fin
        #     # template_name = 'ganaderia/animal_agregar.html'
        #     # while True:
        #     # leemos hasta que encontarmos el final de linea
        #     sArduino = PuertoSerie.readline()
        #     # Mostramos el valor leido y eliminamos el salto de linea del final
        #     print "Valor Arduino: " + sArduino.rstrip('\n')
        #     nfc = sArduino.rstrip
        #     # xdxd = {'model':model}
        #     contexto = {'nfc':nfc,'model':model}	
        #     return render(request, 'ganaderia/animal_agregar.html',contexto)
        #     # return { "form": form}

