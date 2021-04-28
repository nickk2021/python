"""
Ejercicio 4: 
crear un scrip que tenga 4 variables, una lista, un string,
un entero, un booleano y que imprima un mensaje
segun el typo de dato
"""
def comprobartipado(dato, tipo):
    test = isinstance(dato, tipo)
    result = ""

    if test:
        print(f"Este dato es del tipo {type(dato)}")
    else:
        result= None
    return result


mi_lista = ["Hola mundo", 77]
titulo = "Master en python"
numero = 100
verdadero = True

print(comprobartipado(mi_lista, list))
print(comprobartipado(titulo, list))
print(comprobartipado(numero, list))
print(comprobartipado(verdadero, list))