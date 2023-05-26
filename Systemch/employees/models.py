from django.db import models

# Create your models here.
class Rol(models.Model):
    rol_cargo = models.CharField(max_length=60)
    telefono = models.CharField(max_length=12)
    email = models.CharField(max_length=70)
    pais = models.CharField(max_length=70)

    # Define methods str
    def __str__(self):
        return f'Rol del equipo de trabajo {self.id}: {self.rol_cargo} {self.telefono} {self.email} {self.pais}'

class Registro(models.Model):
    codigojira = models.CharField(max_length=150)
    nombre = models.CharField(max_length=70)
    horas = models.FloatField(max_length=10)
    fecha = models.CharField(max_length=11) #models.auto_now_add=True
    rol = models.ForeignKey(Rol, on_delete=models.SET_NULL, null=True)  # related into two tables

    def __str__(self):
        #text = '{0}{1}{2}{3}{4}'
        #return text.format(self.id, self.codigojira, self.nombre, self.horas, self.fecha)
        return f'Registros {self.id}: {self.codigojira}, {self.nombre}, {self.horas}, {self.fecha}'