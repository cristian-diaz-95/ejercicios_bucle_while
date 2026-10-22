"""
Caso. Un curso recibe notas entre 0 y 100, una a una, hasta recibir -99. Muestre la cantidad de notas y
su promedio. El centinela no es una nota y no participa en el cálculo. Si aparece primero, muestre
cantidad cero y «Sin notas» en lugar de un promedio. El flujo siempre contiene -99. El promedio es la
suma de las notas aceptadas dividida entre su cantidad.
Fórmula o relación: Promedio = suma de las notas / cantidad de notas, solo cuando la cantidad sea
positiva.
"""
nota=0
contador=0
while nota!=-99:
    nota_ingre=int(input("ingrese una nota: "))
    if nota_ingre==-99:
        break
    else:
        contador+=1
        nota+=nota_ingre
print("cantidad: ",contador)
if nota==0:
    print("sin notas")
else: 
    print("promedio: ",nota/contador)