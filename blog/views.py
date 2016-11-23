from django.shortcuts import render
from django.contrib import messages
from .forms import PeliculaForm
from blog.models import Compra, Producto, Persona, Marca,CD

def pelicula_nueva(request):
    if request.method == "POST":
        formulario = PeliculaForm(request.POST)
        if formulario.is_valid():
            pelicula = Compra.objects.create(cantidad = formulario.cleaned_data['cantidad'],persona=formulario.cleaned_data['persona'])
            for compra_id in request.POST.getlist('productos'):
                actuacion = CD(compra_id = compra_id, producto_id = pelicula.id)
                actuacion.save()

            messages.add_message(request, messages.SUCCESS, 'Pelicula Guardada Exitosamente')
    else:
        formulario = PeliculaForm()
    return render(request, 'productos/Pelicula_editar.html', {'formulario': formulario})
# Create your views here.
