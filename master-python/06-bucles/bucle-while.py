"""

#BUCLE WHILE
Estrucrutra de control que itera o repita la ejecucion de una 
serie de intrusciones tanta veces como sea necesario,
hasta que deje de cumplirse la condicion

#while condicion:
bloque de instrucciones 
actualizacion de contador




"""
contador = 1 
while contador <= 100 :
    print(f"estoy en el numero: {contador}")
    contador = contador + 1

print("----------------------------")

contador = 1
muestrame = str(0)
while contador <= 100 :
   muestrame = muestrame + ", " + str(contador)
   contador = contador + 1
   print(muestrame)

#ejemplo

print("#### ejemplo ####")
numero_usuario = int(input("¿De que numero quieres la tabla?: "))


if numero_usuario < 1:
     numero_usuario = 1 
    
print(f"### tabla del {numero_usuario} ###")
    

contador = 1
while contador <= 10:
    print(f"{numero_usuario} x {contador} = {numero_usuario*contador}")
    contador += 1

else:
    print("tabla terminada!!")