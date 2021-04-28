"""
Diccionario: 
un tipo de dato que almacena un conjunto de datos.
en formato clave > valor.
Es parecido aun array asociativo o un objeto json.

"""
persona = {
    "nombre": "Pablo",
    "apellido": "Rojas",
    "web":"Pablorojas.ar"
}

print(persona["apellido"])

# LISTAS CON DICCIONARIOS
contactos = [
    {
        "nombre": "Antonio",
        "email": "Amtonio@antonio.com"
    },
    {
        "nombre": "Alberto",
        "email": "Alberto@alberto.com"
    },
    {
        "nombre": "Juan",
        "email": "Juan@juan.com"
    }
]
contactos[0]["email"] = "antoñito@antoñito.com"
print(contactos[1]["email"])

print("\nListado de contactos: ")

for contacto in contactos:
    print(f"Nombre del contacto: {contacto['nombre']}")
    print(f"email del contacto: {contacto['email']}")
    print("----------------------------")