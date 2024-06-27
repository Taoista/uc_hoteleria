# Importa el modelo TipoHabitacion
from app1.models import TipoHabitacion

def crear_seeds():
    # Crear dos instancias de TipoHabitacion y guardarlas en la base de datos
    habitacion_simple = TipoHabitacion(
        id_hotel=1,  # ID del hotel al que pertenece esta habitación
        estado=1,
        tipo='simple',
        capacidad=1,
        camas=1,
        banos=1,
        precio=50000  # Precio en CLP
    )
    habitacion_simple.save()

    habitacion_suite = TipoHabitacion(
        id_hotel=1,  # ID del hotel al que pertenece esta habitación
        estado=1,
        tipo='doble',
        capacidad=2,
        camas=2,
        banos=1,
        precio=70000  # Precio en CLP
    )
    habitacion_suite.save()

    habitacion_suite = TipoHabitacion(
        id_hotel=2,  # ID del hotel al que pertenece esta habitación
        estado=1,
        tipo='simple',
        capacidad=1,
        camas=1,
        banos=1,
        precio=45000  # Precio en CLP
    )
    habitacion_suite.save()

    habitacion_suite = TipoHabitacion(
        id_hotel=2,  # ID del hotel al que pertenece esta habitación
        estado=1,
        tipo='doble',
        capacidad=2,
        camas=2,
        banos=1,
        precio=75000  # Precio en CLP
    )
    habitacion_suite.save()

    print('Seeds creados exitosamente.')

# Llamar a la función para crear los seeds cuando se ejecute este script
crear_seeds()
