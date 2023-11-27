
from rest_framework.routers import DefaultRouter
from django.urls import path, include

from . import views


app_name = 'core'

router = DefaultRouter()

urlpatterns = [
    path('create/', views.CreateUserView.as_view(), name='create-user'),
    path('login/', views.CreateTokenView.as_view(), name='auth-login'),
    path('me/', views.ManageUserView.as_view(), name='me'),
    path('', include(router.urls)),
]
