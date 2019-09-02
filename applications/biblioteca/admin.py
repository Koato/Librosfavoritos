from django.contrib import admin

# Register your models here.
from .models import Autor, Libros

#agrega mas opciones a la vista (adornos)
class AutorAdmin(admin.ModelAdmin):
	list_display = (
		'nombre',
		'nacionalidad',
		'id',
	)
	#buscar por campo
	search_fields = ('nombre', 'nacionalidad',)

#agrega mas opciones a la vista (adornos)
class LibrosAdmin(admin.ModelAdmin):
	list_display = (
		'title',
		'resume',
		'autor',
	)
	#buscar por campo
	search_fields = ('title', 'resume', 'autor')
	#filtros 
	list_filter = ('autor',)

#administrar desde web
admin.site.register(Autor, AutorAdmin)
admin.site.register(Libros, LibrosAdmin)