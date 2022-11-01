"""codigum URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.urls import path
from. import views

urlpatterns = [
    path('hola/', views.hola),
    path("mis-familiares/", views.familiares),
    path('la-fecha/', views.fecha),
    path('fecha-nacimiento/<int:edad>', views.dateborn),
    path('template/', views.primertemplate),
    path('template/<str:nombre>/', views.segundotemplate),
    path('new-template/', views.probandotemplate),
    path('ver-familiares/', views.ver_persona),
    path('crear-familiares/<str:nombre>/<str:apellido>/<int:edad>/', views.crear_persona),
    path('admin/', admin.site.urls),
]
