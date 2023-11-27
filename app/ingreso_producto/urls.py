
from django.urls import path, include
from rest_framework.routers import DefaultRouter

from . import views


app_name = 'ingreso_producto'


router = DefaultRouter()
router.register('plantas', views.PlantaViewSet)
router.register('productos', views.ProductoViewSet)
router.register('proveedores', views.ProveedorViewSet)
router.register('ingreso_producto', views.IngresoProductoViewSet)
router.register('tipo_ingreso', views.TipoIngresoViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
