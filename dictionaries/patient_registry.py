#Elaborar un programa con datos de pacientes de una clínica que permita:
#Agregar paciente
#Verificar paciente

pacientes={102:"Maria",195:"Saul",127:"Pedro",29:"Sofia"}

cod=int(input("Ingrese el codigo del paciente: "))
if cod in pacientes:
    print("El paciente ya esta registrado!")
else:
    nom=input("Ingrese el nombre del paciente: ")
    pacientes[cod]=nom
    print("Paciente agregado exitosamente !")
    print("-",45)
    print("Lista actualizada: ", pacientes)
    
print("Fin del programa")
