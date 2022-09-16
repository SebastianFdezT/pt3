from django.db import models
from django.contrib.auth.models import User

class Prueba(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    nombre_prueba = models.CharField('Nombre Prueba', max_length=100)

    def __str__(self):
        return str(self.id) + '-' + self.nombre_prueba

class Tema(models.Model):
    nombre_tema = models.CharField('Nombre Tema', max_length=100)

    def __str__(self):
        return str(self.id) + '-' + self.nombre_tema

class Preguntas(models.Model):
    prueba = models.ForeignKey(Prueba, on_delete=models.CASCADE)
    tema = models.ForeignKey(Tema, on_delete=models.CASCADE)

    pregunta = models.CharField('Pregunta', max_length=100)
 
    def __str__(self):
        return str(self.id) + '-' + self.pregunta

class Curso(models.Model):
    nombre_curso = models.CharField('Nombre del Curso', max_length=100)

    def __str__(self):
        return self.nombre_curso        

class Estudiante(models.Model):
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE)

    nombres = models.CharField('Nombres', max_length=20)
    apellidos = models.CharField('Apellidos', max_length=20)
    nombre_completo = models.CharField('Nombre Completo', max_length=40, blank=True)
    
    preguntas = models.ManyToManyField(Preguntas,through='EstudiantePreguntas', blank=True)

    #class Meta:
    #    verbose_name = 'Estudiante'
    #    verbose_name_plural = 'Estudiantes del curso'
    #    ordering = ['-nombres', 'apellidos']

    def __str__(self):
        return self.nombres + ' ' + self.apellidos

class EstudiantePreguntas(models.Model):
    estudiante = models.ForeignKey(Estudiante, on_delete=models.CASCADE, blank=True, null=True)
    preguntas = models.ForeignKey(Preguntas, on_delete=models.CASCADE, blank=True, null=True)

    correcto = models.BooleanField(null=True)

    def __str__(self):
        return str(self.id) + '-' + self.estudiante.nombres