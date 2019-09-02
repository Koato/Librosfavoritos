from django.shortcuts import render

# Create your views here.
from django.views.generic import (
	TemplateView,
	ListView,
)

from .models import Autor, Libros

class ListaAutores(ListView):
	template_name = 'biblioteca/lista-autores.html'
	model = Autor
	context_object_name = 'autores'