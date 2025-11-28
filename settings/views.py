from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required

def home(request):
    """Vista raíz que renderiza la página de inicio."""
    return render(request, 'home.html')

def login_view(request):
    """Vista de login para obtener token JWT."""
    # Si ya está autenticado, redirigir a productos
    if request.user.is_authenticated:
        return redirect('products')
    return render(request, 'login.html')

def products(request):
    """Vista que renderiza la página de productos."""
    # Verificar si tiene token en localStorage (esto se hace en el cliente con JS)
    return render(request, 'products.html')

def orders(request):
    """Vista que renderiza la página de pedidos."""
    # Verificar si tiene token en localStorage (esto se hace en el cliente con JS)
    return render(request, 'orders.html')
