from django.urls import path
from . import views

urlpatterns = [
    path('', views.bienvenida, name="bienvenida"),
    path('listacursos/', views.listacursos, name="listacursos"),
    path('crear-curso/', views.crearCurso, name="crear-curso"),
    path('actualizar-curso/<str:pk>/', views.actualizarCurso, name="actualizar-curso"),
    path('eliminar-curso/<str:pk>/', views.eliminarCurso, name="eliminar-curso"),
    path('curso/<str:pk>', views.curso, name="curso"),
    path('crear-estudiante/<str:pk>', views.crearEstudiante, name="crear-estudiante"),
    path('actualizar-estudiante/<str:pk>/', views.actualizarEstudiante, name="actualizar-estudiante"),
    path('eliminar-estudiante/<str:pk>/', views.eliminarEstudiante, name="eliminar-estudiante"),
    path('prueba/', views.prueba, name="prueba"),
    path('crear-prueba/', views.crearPrueba, name="crear-prueba"),
    path('actualizar-prueba/<str:pk>/', views.actualizarPrueba, name="actualizar-prueba"),
    path('eliminar-prueba/<str:pk>/', views.eliminarPrueba, name="eliminar-prueba"),
    path('preguntas/<str:pk>', views.preguntas, name="preguntas"),
]