"""
ejercicio 1. hacer un programa que tenga una lista de 8 numeroenteros y haga lo siguiente:
- recorrer la lista y mostrarla.
- ordenarla y mostrarla
- mostrar su longitud
- buscar algun elemento (que el usuario pida por teclado) 
"""
# crear la lista
numeros =[13, 64, 52, 79, 21, 7, 91, 63]

# Crear funcion que recorra lista y devuelva string
def mostrarLista(lista):
    resultado = ""

    for elemento in lista:
        resultado += str(elemento)
        resultado +="\n"

    return resultado



# recorrer y mostrar
"""
print("#### recorrer y mostar ####")
for numero in numeros:
    print(numero)
"""
print(mostrarLista(numeros))
print("\n")

# Ordenar y mostrar
print("#### ordenar y mostar ####")

numeros.sort()
print(mostrarLista(numeros))

print("\n")

# Mostrar su longitud
print("#### Mostrar su longitud  ####")
print(len(numeros))

print("\n")

# Busqueda en la lista
try:

    print("#### Busqueda en la lista  ####")
    busqueda = int(input("Introduce el numero: "))

    comprobar= isinstance(busqueda, int)
    while not comprobar or busqueda <= 0:
        busqueda =int(input("Introduce el numero: "))
    else:
        print(f"Has introducido el {busqueda}")

    print(f"###  Buscar en la lista el numero {busqueda} ###")
    
    search =numeros.index(busqueda)
       
    print(f"El numero busacado en la lista es el indice: {search}")
        
except:
        print("El numero no esta en la lista")