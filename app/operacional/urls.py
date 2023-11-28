
from django.urls import path, include
from rest_framework.routers import DefaultRouter


app_name = 'operacional'

from operacional.api.viewset.ingreso_producto_viewset import IngresoProductoViewSet
from operacional.api.viewset.planta_viewset import PlantaViewSet
from operacional.api.viewset.producto_viewset import ProductoViewSet
from operacional.api.viewset.proveedor_viewset import ProveedorViewSet
from operacional.api.viewset.tanque_viewset import TanqueViewSet
from operacional.api.viewset.tipo_ingreso_viewset import TipoIngresoViewSet
from operacional.api.viewset.tipo_tanque_viewset import TipoTanqueViewSet
from operacional.api.viewset.calidad_viewset import CalidadViewSet
from operacional.api.viewset.tipo_muestra_viewset import TipoMuestraViewSet
from operacional.api.viewset.ingreso_producto_tanque_viewset import IngresoProductoTanqueViewSet


router = DefaultRouter()
router.register('tanques', TanqueViewSet)
router.register('tipo_tanque', TipoTanqueViewSet)
router.register('plantas', PlantaViewSet)
router.register('productos', ProductoViewSet)
router.register('proveedores', ProveedorViewSet)
router.register('ingreso_producto', IngresoProductoViewSet)
router.register('tipo_ingreso', TipoIngresoViewSet)
router.register('calidades', CalidadViewSet)
router.register('tipo_muestra', TipoMuestraViewSet)
router.register('ingreso_producto_tanque', IngresoProductoTanqueViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
