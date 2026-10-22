"""
Caso. Una actividad recibe dos enteros A y B con A < B. Muestre, en orden ascendente, todos los enteros
estrictamente mayores que A y menores que B. Los extremos no se muestran. Si no hay enteros entre
ellos, informe «No hay enteros interiores».
Fórmula o relación: Cada entero consecutivo difiere del anterior en 1.
"""
a=int(input("ingrese entero A: "))
b=int(input("ingrese entero B: "))
if a==b or a+1==b:
    print(" no hay enteros interiores")
else:
    while  a<b:
        for i in range(a+1,b):
            print(i)
        break