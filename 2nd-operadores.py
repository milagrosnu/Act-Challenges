Nombre_Alumno = (input("Ingrese nombre del alumno: "))

Nota_1 = float(input("Ingrese valor de primer nota: "))
Nota_2 = float(input("Ingrese valor de segunda nota: "))
Nota_3 = float(input("Ingrese valor de tercer nota: "))

#nota media: suma / cantidad
Nota_Media = (Nota_1 + Nota_2 + Nota_3) / 3
#nota final: suma de porcentajes
Nota_Final = (Nota_1 * 0.15 + Nota_2 * 0.35 + Nota_3 * 0.50) 

print(f"La nota media de {Nombre_Alumno} es {Nota_Media}")
print(f"La nota final de {Nombre_Alumno} es {Nota_Final}")