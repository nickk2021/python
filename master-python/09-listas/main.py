"""
LISTAS (arrays)
son colecciones o conjuntos de datos/valores, bajo un unico
nombre.
para acceder a esos valores podemos usar un indice numerico.

"""

pelicula = "batman"

# definir lista
pelicula = ["batman", "spidemar", "el señor de los anillos"]
cantantes = list(("2pac", "drake", "eminem"))
years = list(range(2021, 2030))
variada = ["victor", 3.4, True, "texto"] 
"""
print(pelicula)
print(cantantes)
print(years)
print(variada)
"""
"""
#Indices
print(pelicula[1])
print(pelicula[-2])

# Añadir elementos a una lista
cantantes.append("daddy yanke")
print(cantantes)


# Recorrer lista

print("\n****** Listado Pelicula *******")

for pelicula in pelicula:
    print(f"{pelicula.index(pelicula) + 1}. {pelicula}")
"""
# Listas multidisionales
print("\n*********** Listado de contacto *************")
contactos = [
    [
    "Alberto",
    "alberto@alberto.com"   
    ],
    [
    "juan",
    "juan@juan.com"

    ],
    [
    "Carlos", 
    "carlos@carlos.com"
    ]
]
for contacto in contactos:
    for elemento in contacto:
        if contacto.index(elemento) == 0:
            print("nombre: " + elemento)
        else:
            print("Email: " + elemento)

        