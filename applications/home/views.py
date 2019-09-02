from django.shortcuts import render

# Create your views here.
from django.views.generic import (
	TemplateView,
	ListView,
)

class IndexView(TemplateView):
	template_name = "home/index.html"
	#print('++++ prueba url ++++')

class ListaLibros(ListView):
	template_name = 'home/lista.html'
	queryset = ['Kotlin', 'Java', 'Django', 'Python']
	context_object_name = 'libros'