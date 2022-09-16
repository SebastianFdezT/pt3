from django.shortcuts import render, redirect
from .models import Curso, Estudiante, Preguntas, Prueba
from .forms import CursoForm, EstudianteForm, PruebaForm

def bienvenida(request):
    return render(request, 'base/bienvenida.html')

def listacursos(request):
    cursos = Curso.objects.all()
    context = {'cursos': cursos}
    return render(request, 'base/listacursos.html', context)

def crearCurso(request):
    form = CursoForm()
    if request.method == 'POST':
        form = CursoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listacursos')
    context = {'form': form}
    return render(request, 'base/curso_form.html', context)

def actualizarCurso(request, pk):
    curso = Curso.objects.get(id=pk)
    form = CursoForm(instance=curso)
    if request.method == 'POST':
        form = CursoForm(request.POST, instance=curso)
        if form.is_valid():
            form.save()
            return redirect('listacursos')
    context = {'form': form}
    return render(request, 'base/curso_form.html', context)

def eliminarCurso(request, pk):
    curso = Curso.objects.get(id=pk)
    if request.method == 'POST':
        curso.delete()
        return redirect('listacursos')
    return render(request, 'base/delete.html', {'obj':curso})

def curso(request, pk):
    curso = Curso.objects.get(id=pk)
    context = {'curso': curso}
    return render(request, 'base/curso.html', context)

def crearEstudiante(request, pk):
    curso = Curso.objects.get(id=pk)
    context = {'curso': curso}
    form = EstudianteForm()
    if request.method == 'POST':
        form = EstudianteForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'base/curso.html', context)
    context = {'form': form}
    return render(request, 'base/curso_form.html', context)

def actualizarEstudiante(request, pk):
    estudiante = Estudiante.objects.get(id=pk)
    form = EstudianteForm(instance=estudiante)
    if request.method == 'POST':
        form = EstudianteForm(request.POST, instance=estudiante)
        if form.is_valid():
            form.save()
            return redirect('listacursos')
    context = {'form': form}
    return render(request, 'base/curso_form.html', context)

def eliminarEstudiante(request, pk):
    estudiante = Estudiante.objects.get(id=pk)
    if request.method == 'POST':
        estudiante.delete()
        return redirect('listacursos')
    return render(request, 'base/delete.html', {'obj':estudiante})

def prueba(request):
    pruebas = Prueba.objects.all()
    context = {'pruebas': pruebas}
    return render(request, 'base/prueba.html', context)

def crearPrueba(request):
    form = PruebaForm()
    if request.method == 'POST':
        form = PruebaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('prueba')
    context = {'form': form}
    return render(request, 'base/curso_form.html', context)

def actualizarPrueba(request, pk):
    prueba = Prueba.objects.get(id=pk)
    form = PruebaForm(instance=prueba)
    if request.method == 'POST':
        form = PruebaForm(request.POST, instance=prueba)
        if form.is_valid():
            form.save()
            return redirect('prueba')
    context = {'form': form}
    return render(request, 'base/curso_form.html', context)

def eliminarPrueba(request, pk):
    prueba = Prueba.objects.get(id=pk)
    if request.method == 'POST':
        prueba.delete()
        return redirect('prueba')
    return render(request, 'base/delete.html', {'obj':prueba})  

def preguntas(request, pk):
    preguntas = Preguntas.objects.get(id=pk)
    context = {'preguntas': preguntas}
    return render(request, 'base/preguntas.html', context)