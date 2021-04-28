"""
Ejercicio 2: escribir unprograma que añada valores a una lista 
mientras que su longitu sea menor a 120 y luego mostrar la lista 
plus: usar while y for 
"""
"""

coleccion = []

for contador in range(0, 120):
    coleccion.append(f"elemento-{contador}")
    print("mostrando el : " + coleccion[contador])

print(coleccion)
"""
coleccion = []
x = 0 

while x < 120:
    coleccion.append(f"elemento-{x}")
    print("mostrando el: " + coleccion[x])
    x += 1

print(coleccion[77])