from django.db import models

# Create your models here.
# Tabla a crear
class Autor(models.Model):
	nombre = models.CharField('Nombres', max_length=80)
	nacionalidad = models.CharField(blank=True, max_length=100)

	def __str__(self):
		return self.nombre

# Tabla relacional a Autor
class Libros(models.Model):
	title = models.CharField('titulo', blank=False, max_length=150)
	resume = models.TextField('Resumen', blank=True)
	#restriccion de anexo
	autor = models.ForeignKey(Autor, on_delete=models.CASCADE)

	def __str__(self):
		return self.title
		