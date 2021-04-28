"""
SET es un tipo de dato, para tener una coleccion de valores,
perono tiene ni indice ni orden

"""

personas = {
    "victor",
    "Manolo",
    "Andres"
}
personas.add("Adriana")
personas.remove("Manolo")

print(type(personas))
print(personas)