from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Libro
from .forms import RecomendacionForm
from django.contrib import messages



# Create your views here.
def home(request):
    return render(request, 'index.html')

def inventio_somos_todos(request):
    return render(request, 'inventio_somos_todos.html')

def libros_lista(request):
    libros = Libro.objects.all()
    return render(request, 'libros_lista.html', {'libros_lista': libros})

def recomendaciones(request):
    form = RecomendacionForm()
    if request.method == "POST":
        form = RecomendacionForm(request.POST)
        if form.is_valid():
            recomendacion = form.save(commit=False)

            if request.POST.get("radioDefault") == "no":
                recomendacion.nombre_usuario = None
            
            recomendacion.save()
            messages.success(request, "¡Gracias por tu recomendación!")
    context = {
        'form':form,
        'messages': messages.get_messages(request)
    }
    return render(request, 'recomendaciones.html', context)

def detalle_libro(request, libro_id):
    libro = get_object_or_404(Libro, id=libro_id)
    return render(request, 'detalle_libro.html', {'libro': libro})


