from django.db import models

# Create your models here.

class Hoteles(models.Model):
    id_hotel = models.AutoField(db_column='id', primary_key=True) 
    nombre = models.CharField(max_length=100)
    ubicacion = models.CharField(max_length=255)
    cantidad = models.IntegerField()
    
    def _str_(self):
        return self.nombre

class TipoHabitacion(models.Model):
    id_tipo_habitacion = models.AutoField(db_column='id', primary_key=True)
    id_hotel = models.ForeignKey(Hoteles, on_delete=models.CASCADE)
    estado = models.BooleanField()  # Estado de la habitación (0 o 1)
    tipo = models.CharField(max_length=20)  # Tipo de habitación (ej. Simple, Doble, Suite)
    capacidad = models.IntegerField()  # Capacidad máxima de personas
    camas = models.IntegerField()  # Número de camas
    banos = models.IntegerField()  # Número de baños
    precio = models.IntegerField() # ? precio chileno CLP
    
    class Meta:
        db_table = 'app1_tipo_habitaciones'

    def _str_(self):
        return "creado"

class CantidadTipoHabitacion(models.Model):
    id_cant_tipo_habitacion = models.AutoField(db_column='id', primary_key=True)
    id_hotel = models.ForeignKey(Hoteles, on_delete=models.CASCADE)
    id_tipo_habitacion = models.IntegerField()
    cantidad_habitacion = models.IntegerField()

    class Meta:
        db_table = 'app1_cantidad_tipo_habitacion'
    
    def _str_(self):
        return "creado"


class Servicios(models.Model):
    id_sercicio = models.AutoField(db_column='id', primary_key=True)
    id_hotel = models.ForeignKey(Hoteles, on_delete=models.CASCADE)
    estado = models.BooleanField()
    servicio = models.CharField(max_length=20)  # Tipo de habitación (ej. Simple, Doble, Suite)
    precio = models.IntegerField()










# class Habitacion(models.Model):
#     id_habitacion  = models.AutoField(db_column='id', primary_key=True)
#     hotel = models.ForeignKey(Hoteles, on_delete=models.CASCADE)
#     tipo_habitacion = models.ForeignKey(TipoHabitacion, on_delete=models.SET_NULL, null=True)
#     numero = models.CharField(max_length=10)
#     capacidad = models.IntegerField()
#     precio_por_dia = models.DecimalField(max_digits=10, decimal_places=2)
#     historial_precios = models.JSONField(default=list)  # Guarda cambios de precios en formato JSON
    
#     def _str_(self):
#         return f"{self.hotel.nombre} - {self.numero}"

# class ServicioExtra(models.Model):
#     id_servicioextra  = models.AutoField(db_column='id', primary_key=True)
#     nombre = models.CharField(max_length=100)
#     descripcion = models.TextField()
#     precio_diario = models.DecimalField(max_digits=10, decimal_places=2)
    
#     def _str_(self):
#         return self.nombre

# class Reserva(models.Model):
#     id_reserva  = models.AutoField(db_column='id', primary_key=True)
#     habitacion = models.ForeignKey(Habitacion, on_delete=models.CASCADE)
#     cliente = models.CharField(max_length=100)  # Aquí podrías tener un modelo Cliente más complejo
#     fecha_inicio = models.DateField()
#     fecha_fin = models.DateField()
#     servicios_extras = models.ManyToManyField(ServicioExtra, blank=True)
#     precio_total = models.DecimalField(max_digits=10, decimal_places=2)
    
#     def _str_(self):
#         return f"Reserva de {self.cliente} en {self.habitacion}"

# class CentroEvento(models.Model):
#     id_centroevento  = models.AutoField(db_column='id', primary_key=True)
#     hotel = models.ForeignKey(Hoteles, on_delete=models.CASCADE)
#     nombre = models.CharField(max_length=100)
#     descripcion = models.TextField()
#     capacidad = models.IntegerField()
    
#     def _str_(self):
#         return f"{self.hotel.nombre} - {self.nombre}"

# class ArriendoEvento(models.Model):
#     id_arriendoevento  = models.AutoField(db_column='id', primary_key=True)
#     centro_evento = models.ForeignKey(CentroEvento, on_delete=models.CASCADE)
#     cliente = models.CharField(max_length=100)  # Aquí podrías tener un modelo Cliente más complejo
#     fecha = models.DateField()
#     duracion_horas = models.IntegerField()
#     precio_total = models.DecimalField(max_digits=10, decimal_places=2)
    
#     def _str_(self):
#         return f"Arriendo de {self.cliente} en {self.centro_evento} el {self.fecha}"
