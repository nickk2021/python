# """
# # condicinal IF
# SI se_secumple_esta_condicion:
#     Ejecutar grupo de instrucciones
# SI NO:
#     se ejecutan otro grupo mde instrucciones
# if condicion:
#     instrucciones
# else:
#     otras instrucciones    
# """
#ejemplo1
print("############# EJEMPLO  1 ######")
  
color = "Rojo"
#color = input("Adivina cual es mi color favorito:")

if color =="rojo":
    print("Enhorabuena!!")
    print("El color es ROJO")
else:
    print("color Incorrecto")   

#EJEMPLO 2
print("\n############ Ejemplo 2 #######")

year = 2021
#year = int(input("¿En que año estamos?"))

if year >= 2021:
    print("Estamos en 2021 en adelante!!")
else:
    print("Es un año anterior al 2021")


#EJEMPLO 3

print("\n############ Ejemplo 3 #######")

nombre = "Pablo Rojas"
ciudad = "Buenos Aires"
continente = "America Latina"
edad = 40
mayoria_edad = 18

if edad >= mayoria_edad:
    print(f"{nombre}  es mayor de edad!!")

    if continente !="America Latina":
        print("el usuario No es de America Latina")
    else:
        print(f"Es de America Latina y de {ciudad}") 
else:
    print(f"{nombre} NO es mayor de edad")


#EJEMPLO 4

print("\n############ Ejemplo 4 #######")


#dia = int(input("introduce el numero del dia de la semana"))
dia = 3
if dia== 1:
    print("es lunes")
elif dia== 2:
    print("es martes")
elif dia== 3:
    print("es miercoles")
elif dia== 4:
    print("es jueves")
elif dia== 5:
    print("es viernes")
else:
    print("es finde semana!!")



#EJEMPLO 5          

print("\n############ Ejemplo 5 #######")   

edad_minima = 18
edad_maxima = 65
#edad_oficial = int(input("¿tienes edad de trabajar? Introduce tu edad: "))
edad_oficial = 18
if edad_oficial >= 18 and edad_oficial <= 65:
    print("esta en edad de trabajar!!")
else:
    print("no esta en edad de  trabajar")



#EJEMPLO 6      

print("\n############ Ejemplo 6 #######")
pais = "españa"

if pais =="mexico" or pais == "españa" or pais == "colombia":
    print(f"{pais} es un pais de habla hispana !!")
else:
    print(f"{pais} no es un pais de habla hispana :(")

#EJEMPLO 7     

print("\n############ Ejemplo 7 #######")

pais = "españa"
if not (pais =="mexico" or pais == "españa" or pais == "colombia"):
    print(f"{pais}  NO es un pais de habla hispana !!")
else:
    print(f"{pais} SI es un pais de habla hispana :(")




#EJEMPLO 8     

print("\n############ Ejemplo 8 #######")

pais = "argentina"
if pais !="mexico" and pais != "españa" and pais != "colombia":
    print(f"{pais}  NO es un pais de habla hispana !!")
else:
    print(f"{pais} SI es un pais de habla hispana :(")