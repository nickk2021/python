"""
FUNCIONES 
Una funcion es un conjunto de instrucciones agrupadas bajo
un nombre concreto que pueden reutilizarse ivocandoa 
la funcion tantas veces sea necesariao.

def nombreDeMiFuncion(parametro):
      # BLOQUE / CONJUNTO DE INSTRUCCIONES 

nombreDeMiFuncion(mi_parametro)


"""

"""
#EJEMPLO 1
print("##### ejemplo 1 ##### ")


# definir funcion
def muestraNombre():
    print("Pablo")
    print("Nicolas")
    print("Iñaki")
    print("Patricio")
    print("Paola")
    print("Martina")
    print("\n")

# invocar funcion

muestraNombre()


# Ejemplo 2: parametros

print("######## ejemplo 2 ###########")

def mostrarTuNombre(nombre, edad):
    print(f"Tu nombre es {nombre}")
    if edad >=18:
        print("eres mayor de edad")
    else:
        print("eres menor de edad")
nombre = input("¿Cual es tu nombre?: ")
edad = int(input("Introduce tu edad: ")) 
mostrarTuNombre(nombre, edad)


print("\n")
"""
"""
# Ejemplo 3

print("############# ejemplo 3 ########")

def tabla(numero):
    print(f"tabla de multiplicar del número: {numero}")

    for contador in range(11):
        operacion = numero*contador
        print(f"{numero} x {contador}= {operacion}")

        print("\n")

tabla(3)

#ejemplo3.1
for numero_tabla in range(1, 11):
    tabla(numero_tabla)



# EJEMPLO 4

print("######## ejemplo 4 ######")

#parametros opcionales 

def getEmpleado(nombre, dni = None ):
    print("EMPLEADO")
    print(f"Nombre: {nombre}")

    if dni != None:
        print(f"DNI: {dni}")

getEmpleado("Pablo Rojas", "3288595")

"""
"""
# EJEMPLO 5: parametros opcionales y retur o devolver datos  
print("##### ejemplo 5 ######")

def calculadora(numero1, numero2, basicas = False):

    suma = numero1 + numero2
    resta = numero1 - numero2
    mutiplicacion = numero1 * numero2
    division = numero1 / numero2
    

    cadena =""
    
    if basicas != False:
        cadena += "suma: " + str(suma)
        cadena += "\n"
        cadena += "resta: " + str(resta)
        cadena += "\n"
    else:
           cadena += "multiplicacion: " + str(mutiplicacion)
           cadena += "\n"
           cadena += "division: " + str(division)
           cadena += "\n"
    return cadena
print(calculadora(56, 5, ))
"""
"""
#EJEMPLO 6

print("#### ejemplo 6 ####")


def getNombre(nombre):
    texto = f"El nombre es: {nombre}"
    return texto

def getapellido(apellido):
    texto = f"El apellido es: {apellido}"
    return texto

def devuelveTodo(nombre, apellido):
    texto = getNombre(nombre) + "\n" + getapellido(apellido)
    return texto

print(devuelveTodo("Pablo", "Rojas"))
"""
"""
#EJEMPLO 7

print("#### ejemplo 7 ####")
dime_el_year = lambda year : f"El año es {year * 10}"
print(dime_el_year(2010))
"""
#EJEMPLO 8

print("#### ejemplo 8 ####")
