contador = 1
aprobadoos = 0
suspendidos = 0

numero_alumnos = int(input("¿Cuantos alumnos tienes?: "))


while contador <= numero_alumnos:
    nota = int(input(f"¿Que nota quieres ponerle al \"alumno {contador}\" ?: "))

    if nota >= 5:
        aprobadoos += 1
    else:
        suspendidos += 1

    contador += 1

print(f"\nAlumnos aprobados: {aprobadoos}")
print(f"Alumnos suspendidos: {suspendidos}")