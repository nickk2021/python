"""

# for
for variable in elemento iterable (lista,rango,etc)


BLOQUE DE INSTRUCCIONES 


"""
contador = 0
resultado = 0
for contador in range(0,10):
    print("voy por el " + str(contador))

    resultado += contador 

print(f"el resultado es : {resultado}")




#EJEMPLOS TABLAS DE MULTIPLICAR
print("\n######### Ejemplo ########")


numero_usuario = int(input("¿De que numero quieres la tabla?: "))


if numero_usuario <1:
    numero_usuario = 1


print(f"\n#### tabla de multiplicar del numero {numero_usuario}###")

for numero_tabla in range(1,11):
    print("no se pueden mostrar numero prohibidos !!")
    break


    print(f"{numero_usuario} x {numero_tabla} = {numero_usuario*numero_tabla}")
else:
    print("tabla finaliza!!")
