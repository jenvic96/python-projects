nota = int(input("Ingrese la nota del alumno (0-100): "))

if nota < 60:
    print("Resultado: Reprobó")
elif nota >= 60 and nota <= 69:
    print("Resultado: Aplazó")
else:
    print("Resultado: Aprobó")
