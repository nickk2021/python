#capurar excepciones y manejar errorer de codigo
# susceptible a fallos/errores
"""
try:
    nombre = input("¿Cual es tu nombre?: ")
    if len(nombre) > 1:
        nombre_usuario ="El nombre es " + nombre
    print(nombre_usuario)
except:
    print("ha ocurrido un error, vuelve a colocar tu nombre")

else:
    print("muchas gracias")
finally:
    print("fin de lla interaccion!!")
    """
"""
# Multiples excepciones
try:
    numero = int(input("Numero para elevarlo al cuadrado: "))
    print("El cuadrado es: " + str(numero*numero))
except TypeError:
    print("debes convertir tus cadenas a enteros en el codigo")
except ValueError:
    print("introduce el numero correcto!!")
"""
# Excepciones personalizada
nombre = input("introduce el nombre: " )
edad = int(input("introduce la edad: "))