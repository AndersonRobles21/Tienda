from django.contrib import admin
from django.urls import path, include
from django.http import JsonResponse
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from . import views

def api_home(request):
    return JsonResponse({'message': 'Welcome to Shop API', 'status': 'running'})

urlpatterns = [
    path('admin/', admin.site.urls),

    # Vistas HTML
    path('', views.home, name='home'),
    path('login/', views.login_view, name='login'),
    path('products/', views.products, name='products'),
    path('orders/', views.orders, name='orders'),

    # JWT
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    # API REST REAL
    path('api/products/', include('products.api_urls')),
    path('api/orders/', include('orders.api_urls')),
]
