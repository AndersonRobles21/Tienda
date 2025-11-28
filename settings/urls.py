"""
URL configuration for shop project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.http import JsonResponse
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from . import views

def api_home(request):
    """Vista raíz de API que devuelve un mensaje de bienvenida."""
    return JsonResponse({'message': 'Welcome to Shop API', 'status': 'running'})

urlpatterns = [
    path('admin/', admin.site.urls),

    # Vistas HTML
    path('', views.home, name='home'),
    path('login/', views.login_view, name='login'),
    path('products/', views.products, name='products'),
    path('orders/', views.orders, name='orders'),

    # API Endpoints
    path('api/', api_home, name='api_home'),
    path('api/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/products/', include('products.urls')),
    path('api/orders/', include('orders.urls')),
    
    # Rutas alternativas sin /api/
    path('products-api/', include('products.urls')),
    path('orders-api/', include('orders.urls')),
]

