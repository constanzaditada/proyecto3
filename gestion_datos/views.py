from django.shortcuts import render, redirect
from .models import Categoria, Producto, Cliente
from .forms import CategoriaForm, ProductoForm, ClienteForm

def agregar_categoria(request):
    if request.method == 'POST':
        form = CategoriaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')  # Cambiar 'index' por el nombre de la vista de la página principal
    else:
        form = CategoriaForm()
    return render(request, 'gestion_datos/agregar_categoria.html', {'form': form})

def agregar_producto(request):
    if request.method == 'POST':
        form = ProductoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')  # Cambiar 'index' por el nombre de la vista de la página principal
    else:
        form = ProductoForm()
    return render(request, 'gestion_datos/agregar_producto.html', {'form': form})

def agregar_cliente(request):
    if request.method == 'POST':
        form = ClienteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')  # Cambiar 'index' por el nombre de la vista de la página principal
    else:
        form = ClienteForm()
    return render(request, 'gestion_datos/agregar_cliente.html', {'form': form})

def buscar(request):
    if request.method == 'POST':
        buscar_texto = request.POST.get('buscar_texto')
        categorias = Categoria.objects.filter(nombre__icontains=buscar_texto)
        productos = Producto.objects.filter(nombre__icontains=buscar_texto)
        clientes = Cliente.objects.filter(nombre__icontains=buscar_texto)
        return render(request, 'gestion_datos/buscar_resultados.html', {'categorias': categorias, 'productos': productos, 'clientes': clientes})
    return render(request, 'gestion_datos/buscar.html')
