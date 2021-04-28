numero = int(input("introduce el numero: "))
porcentaje = int(input(f"que porcentaje quieres sacar de {numero}?: "))

operacion = (numero * (porcentaje/100))
print(f"el {porcentaje}% de {numero} es: {operacion}")