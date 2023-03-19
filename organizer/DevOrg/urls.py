from django.urls import path

from . import views

urlpatterns = [
    path('singup/', views.SingUpView.as_view(), name="singup"),
    path('/', views.device_view, name='device_view'),
    path('add/', views.add_device_view, name='add_device')
]
