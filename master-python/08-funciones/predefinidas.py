nombre = "Pablo Rojas"

# funciones generales
print(type(nombre))


# detectr el tipado
comprobar = isinstance(nombre,str)
if comprobar:
    print(" esa variable es un string")
else:
    print("no es una cadena")

if not isinstance(nombre, float):
    print("La variable no es un numero con decimales")

# Limpiar espacios
frase = "   mi contenido   "
print(frase)
print(frase.strip())

# Eliminar variables

year = 2021
print(year)
del year
#print(year)
# comprobar variable vacia
texto = "ff"

if len(texto) <=0:
    print("la variable esta vacia")
else:
    print("la variable tiene contenido: ", len(texto))


# encontarr caracteres
frase = "la vida es bella"
print(frase.find("vida"))

#Remplazar palabras es un string
nueva_frase = frase.replace("vida","moto")
print(nueva_frase)

#Mayusculs y minusculas
print(nombre)
print(nombre.lower())
print(nombre.upper())





