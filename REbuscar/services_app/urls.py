from django.urls import path
from services_app import views

urlpatterns = [
    path('', views.index, name='REbuscar-home'),
    path('servicios_oficiales/', views.servicios_oficiales, name='servicios_oficiales'),
    path('servicios_locales/', views.servicios_locales, name='servicios_locales'),
    path('service_register/', views.service_register, name='service_register'),
    path('contact/', views.contact, name='contact'),
]