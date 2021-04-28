"""
variables locales: se definen dentro de las funcion y no
se puede usar fuera de ella, solo estan disponibles dentro.
a no ser que hagamos return.
variables globales: son las que se declaran fuera de una funcion 
y estan disponible dentro y fuera de ellas.


"""
"""
# variables global
frase = "Ni los genios son tan genios, ni los medicres tan mediocres "

print(frase )


def holaMundo():
    frase = "hola mundo"
    print("dentro de la funcion: ")
    print(frase)
    

    year = 2021
    print(year)
    global website
    website = "narojas.ar"
   
    return "dato devuelto" + str(year)

print (holaMundo())
print(website)
"""
