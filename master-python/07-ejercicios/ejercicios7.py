numero1 = int(input("introduce un numero: "))
numero2 = int(input("introduce el siguiente numero: "))


if numero1 < numero2:
    for contador in range (numero1, (numero2 + 1)):
        if contador%2 ==0:
            print(f"{contador} es par")
        else:
            print(f"{contador} es impar")

else:
    print("el numero 1 debe ser mayor al numero 2")