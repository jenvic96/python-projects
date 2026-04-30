#Programa


alumnos=["Juan", "Lucia", "Mario", "Victor", "Sofia", "Hugo"]

nom=input("Ingrese el nombre del alumno: ")

if nom in alumnos:
    print("El alumno ya esta matriculado")
else:
    alumnos.append(nom)
    print("Alumno registrado exitosamente ! ")
    print("Nueva lista de alumnos:", alumnos)

print("Fin del programa ! ")
