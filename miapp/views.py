from django.shortcuts import render, HttpResponse, redirect
from django.db.models import Q
from django.contrib import messages
from miapp.models import course
from miapp.models import career

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

def crear_course(request, code, name, hour,credits, state):
    course = course(
        code = code,
        name = name,
        hour = hour,
        credits = credits,
        state = state
    )
    course.save()
    return HttpResponse(f"Curso Creado: {course.code} - {course.name}- {course.hour} - {course.credits} - {course.state}")


def editar_course(request, id):
    course = course.objects.get(pk=id)

    course.titulo = "Enseñanza onLine en la UNTELS"
    course.contenido = "Aula Virtual, Google Meet, Portal Académico, Google Classroom..."
    course.publicado = False

    course.save()
    return HttpResponse(f"Course Editado: {course.titulo} - {course.contenido}")

def listar_course(request):
    course = course.objects.all()
    """
    course = course.objects.filter(
        Q(titulo__contains="Py") |
        Q(titulo__contains="Hab")
    )
    """
    return render(request, 'listar_curso.html',{
        'course': course,
        'titulo': 'Listado de Cursos'
    })
def eliminar_course(request, id):
    course = course.objects.get(pk=id)
    course.delete()
    return redirect('listar_curso')

def save_course(request):
    if request.method == 'POST':
        name = request.POST['name']
        if len(name)<=5:
            return HttpResponse("<h2>El tamaño del título es pequeño, intente nuevamente</h2>")
        code = request.POST['code']    
        hour = request.POST['hour']
        credits = request.POST['credits']    
        state = request.POST['state']        
        course = course(
            code = code,        
            name = name,
            hour = hour,        
            credits = credits,        
            state = state            
        )
        course.save()
        return HttpResponse(f"Curso Creado: {course.name} - {course.code} ")
    else:
        return HttpResponse("<h2> No se ha podido registrar el artículo </h2>")

def crear_course(request):
    return render(request, 'crear_curso.html')



def crear_career(request, name, shortname,image, state):
    career = career(
        name = name,
        shortname = shortname,
        image = image,
        state = state
    )
    career.save()
    return HttpResponse(f"Carrera Creado: {career.name} - {career.shortname}- {career.image} - {career.state}")

def editar_career(request, id):
    career = career.objects.get(pk=id)

    career.name = "Enseñanza onLine en la UNTELS"
    career.shortname = "Aula Virtual, Google Meet, Portal Académico, Google Classroom..."
    career.state = False

    career.save()
    return HttpResponse(f"Carrera Editado: {career.name} - {career.shortname}- {career.image} - {career.state}")

def listar_career(request):
    career = career.objects.all()
    """
    career = career.objects.filter(
        Q(titulo__contains="Py") |
        Q(titulo__contains="Hab")
    )
    """
    return render(request, 'listar_carrera.html',{
        'career': career,
        'titulo': 'Listado de Carreras'
    })

def eliminar_career(request, id):
    career = career.objects.get(pk=id)
    career.delete()
    return redirect('listar_carrera')

def save_career(request):
    if request.method == 'POST':
        name = request.POST['name']
        shortname = request.POST['shotname']
        image = request.POST['image']
        state = request.POST['state']

        career = career(
            name = name,
            shortname = shortname,
            image = image,
            state = state
        )
        career.save()
        return HttpResponse(f"Carrera Creado: {career.name} - {career.shortname}- {career.image} - {career.state}")
    else:
        return HttpResponse("<h2> No se ha podido registrar la carrera </h2>")

def create_career(request):
    return render(request, 'create_carrera.html')