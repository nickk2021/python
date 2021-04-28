numero1 = int(input("introduce el primer numero: "))
numero2 = int(input("introduce el segundo numero: "))

if numero1 < numero2:

    for contador in range(numero1, (numero2 + 1)):
        print(contador)

else:
    print("el numero 1 debe ser menor al numero 2")
