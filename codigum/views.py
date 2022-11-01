from asyncore import read
import email
from pipes import Template
from re import template
from django.http import HttpResponse
from datetime import datetime, timedelta
from django.template import Context, Template, loader
import random

from homeblog.models import Persona


def hola(request):
    return HttpResponse('<h1>My primer MTV en Django!!</h1>')

def familiares(request):
    return  HttpResponse("<h2>Mis familares a mostrar del primer Mtv seran 3!!!</h2>")

def fecha(request):
    fecha_hora = datetime.now()
    return HttpResponse(f"La fecha y hora actual es {fecha_hora}")

def dateborn(request, edad):
    fecha = datetime.now().year- edad
    return HttpResponse(f'<h2>tu fecha de nacimiento aproximada para tu edad {edad} es:{fecha}</h2>')

def primertemplate(request):
    
    cargar_archivo = open(r'C:\Users\Hp\Desktop\CODE\codigum\templates\template.html', 'r')
    template= Template(cargar_archivo.read())
    cargar_archivo.close()
    contexto = Context()
    #cuando no hay parametros lo hago igual
    template_renderizado= template.render(contexto)
    #en este item la renderizo
    #lo digo al template que se renderize para poder ejecutarlo
    
    return HttpResponse(template_renderizado)


def segundotemplate(request, nombre):
        
    template = loader.get_template('template.html')
    
    template_renderizado = template.render({'persona':nombre})
    
    return HttpResponse(template_renderizado)

def probandotemplate(request):
    mi_contexto = {'rango' : range(1, 20), 
                   'aleatorio':random.randrange(0,50)}
    template = loader.get_template('newtemplate.html')
    template_renderizado = template.render(mi_contexto)
    
    
    return HttpResponse(template_renderizado)
############################################################
######## MI MVT#################

#CREANDO UNA PERSONAS EN MI BSE DE DATOS PARA MI MVT

def crear_persona(request, nombre, apellido):
    persona = Persona(nombre=nombre, apellido=apellido, edad=random.randrange(0, 40), fechadenacimiento=datetime.now(),email=email)
    persona.save()
    
    template = loader.get_template('crear_persona.html')
    template_renderizado = template.render({'personas':persona})
    return HttpResponse(template_renderizado)    

##########################################################
def ver_persona(request):
    personas = Persona.objects.all()
    template = loader.get_template('ver_persona.html')
    template_renderizado = template.render({'personas':personas})
    return HttpResponse(template_renderizado)