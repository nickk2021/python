"""
Ejercicio 3: programa que comprube si una variable esta vacia 
y si esta vacia, rellenarlacon texto en minuscula y mostrala 
en mayuscula
"""
texto = ""

if len(texto.strip())<= 0:

    texto = "hola soy n texto en minusculas"
    print(texto.upper())



else:
    print(f"La variable tine contenido {texto}")