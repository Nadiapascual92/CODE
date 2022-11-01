from django.db import models

class Persona(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    edad = models.IntegerField()
    fechadenacimiento= models.DateTimeField()
    email = models.EmailField()
    #si quiero dejar de ingresar la fecha tengo que rellenar
    #el campofechadenacimiento del datetimefield con null=True
    #la terminal me pregunta cuadno modifico la classe que
    #modificare tambien la bbdd