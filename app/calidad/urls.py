
from django.urls import path, include
from rest_framework.routers import DefaultRouter

from . import views


app_name = 'calidad'


router = DefaultRouter()
router.register('calidades', views.CalidadViewSet)
router.register('tipo_muestra', views.TipoMuestraViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
