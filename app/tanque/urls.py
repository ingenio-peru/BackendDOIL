
from django.urls import path, include
from rest_framework.routers import DefaultRouter

from . import views


app_name = 'tanque'


router = DefaultRouter()
router.register('tanques', views.TanqueViewSet)
router.register('tipo_tanque', views.TipoTanqueViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
