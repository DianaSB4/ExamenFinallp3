from django.shortcuts import render, HttpResponse, redirect
from django.db.models import Q
from django.contrib import messages

# Create your views here.


def saludo(request):
    return render(request, 'saludo.html', {
        'titulo': 'Saludo',
        'autor_saludo': 'Mg. Flor Elizabeth Cerdán León'
    })
def index(request):
    estudiantes = [
        'SERGIO DANIEL VITE COCHACHIN',
        'ANTHONY GERARDO BENDEZU SANTISTEBAN',
        'CRISTIAN ALEXIS CHIPANA HUAMAN',
        'CARLOS GUSTAVO OYOLA SAAVEDRA',
        'GERARDO MANUEL CASTILLO TORDOYA'
    ]
    
    return render(request, 'index.html', {
        'titulo': 'Inicio',
        'mensaje': 'Proyecto Web con DJango',
        'estudiantes': estudiantes
    })

def crear_curso(request):
    return render(request, 'crear_curso.html')
def crear_carrera(request):
    return render(request, 'crear_carrera.html')
def listar_curso(request):
    return render(request, 'listar_curso.html')
def listar_carrera(request):
    return render(request, 'listar_carrera.html')


