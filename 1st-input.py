#uso de float para poder ingresar numeros con decimales
nota_1 = float(input("Ingrese nota 1, (pueden incluirse decimales indicados con un punto, ejemplo 8.5): "))
nota_2 = float(input("Ingrese nota 2, (pueden incluirse decimales indicados con un punto, ejemplo 8.5): "))
nota_3 = float(input("Ingrese nota 3, (pueden incluirse decimales indicados con un punto, ejemplo 8.5): "))

puntajes = (nota_1 * 0.20 + nota_2 * 0.3 + nota_3 * 0.5)
print(f"Nota final: {puntajes}")