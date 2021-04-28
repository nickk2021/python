"""
Modulos: son funcionalidades ya hechas para reutilizarla
"""
# importar mi modulo propio
from mimodulo import holaMundo
print(holaMundo("Pablo Rojas"))

# Modulo fechas
import datetime
print(datetime.date.today())


fecha_completa = datetime.datetime.now()
print(fecha_completa)
print(fecha_completa.year)

# Modulo matematicas
import math
print("raiz cuadrada de 10: ", math.sqrt(10))


#modulo random
import random
print("numero aleatorio entre 15 y 67: ", random.randint(15, 67))