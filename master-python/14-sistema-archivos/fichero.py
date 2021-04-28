from io import open
import pathlib
import shutil 

# abrir archivo
ruta =str(pathlib.Path().absolute())+ "/fichero_texto.txt"
archivo = open(ruta, "a+")
# escribir
#archivo.write("******** soy un texto metido desde python*****")

#CERRA EL ARCHIVO
archivo.close()

# abrir archivo
ruta =str(pathlib.Path().absolute())+ "/fichero_texto.txt"
archivo_lectura = open(ruta, "r+")
"""
# leer contenido
contenido = archivo_lectura.read()
print(contenido)
"""
"""
# leer contenido u guarrdar en lista
lista = archivo_lectura.readlines()
archivo_lectura.close()

for frase in lista:
    print("- " + frase.center(10))

# copiar 
ruta_original =str(pathlib.Path().absolute())+ "/fichero_texto.txt"
ruta_nueva =str(pathlib.Path().absolute())+ "/fichero_copiado.txt"
shutil.copyfile(ruta_original, ruta_nueva)
"""
# mover
#ruta_original =str(pathlib.Path().absolute())+ "/fichero_copiado.txt"
#ruta_nueva =str(pathlib.Path().absolute())+ "/fichero_NUEVO.txt"

#shutil.move(ruta_original, ruta_nueva)

# Eliminar
#import os
#ruta_nueva =str(pathlib.Path().absolute())+ "/fichero_NUEVO.txt"
#os.remove(ruta_nueva)

# comprar si existe
import os.path
#print(os.path.abspath("./"))
ruta_comprobar = os.path.abspath("./") + "/fichero_texto.txt"
if os.path.isfile(ruta_comprobar):
    print("el archivo existe")
else:
    print("el archivo no existe")