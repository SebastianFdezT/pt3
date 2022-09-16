from django.forms import ModelForm
from .models import Curso, Estudiante, Prueba

class CursoForm(ModelForm):
    class Meta:
        model = Curso
        fields = '__all__'

class EstudianteForm(ModelForm):
    class Meta:
        model = Estudiante
        fields = '__all__'

class PruebaForm(ModelForm):
    class Meta:
        model = Prueba
        fields = '__all__'