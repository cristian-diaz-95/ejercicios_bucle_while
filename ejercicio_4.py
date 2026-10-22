"""
Caso. Una nómina ficticia recibe primero el salario mensual de un trabajador. Cero termina el registro y
no requiere otros datos. Un salario mensual positivo se acompaña de días trabajados, entero de 0 a 30,
bonos no negativos y otras deducciones no negativas. Muestre el pago neto de cada trabajador, en
orden de lectura. La retención es 5 % y el aporte de seguridad es 12 % del devengado. Se garantiza que
las otras deducciones no superan el devengado después de esos descuentos. El flujo termina con salario

mensual cero. El salario proporcional corresponde al salario mensual multiplicado por los días
trabajados y dividido entre 30. El devengado es ese salario proporcional más los bonos. Tanto la
retención como el aporte se calculan sobre ese mismo devengado: se descuentan en total 17 %, queda
el 83 % y después se restan las otras deducciones. Todos los importes usan la misma unidad monetaria.
Sin trabajadores, informe «Sin trabajadores».
Fórmula o relación: Salario proporcional = mensual × días / 30. Devengado = salario proporcional +
bonos. Neto = devengado × 0,83 - otras deducciones.
"""
nomina=0
salario_mensual=0
dias_trabajados=0
bonos=0
otras_deducciones=0
salario_proporcional=0
salario_devengado=0
salario_neto=0
while True:
    while True:
        salario_mensual=int(input("ingrese el salario mensual del trabajador: "))
        if salario_mensual<0:
            print("valor invalido \n el salario es positivo")
        else:
            break
    if salario_mensual==0:
            break
    while True:
        dias_trabajados=int(input("cantidad de dias trabajados [0,30]: "))
        if dias_trabajados<0 and 30<dias_trabajados:
            print("valor invalido \n Recuerde el rango es 0 a 30")
        else:
            break
    while True:
        bonos=int(input("ingrese el valor del bono: "))
        if bonos<0:
            print("valor invalido \n recuerde el bono no puede ser negativo")
        else:
            break
    while True:
        otras_deducciones=int(input("ingrese otras deducciones: "))
        if otras_deducciones<0:
            print("valor invalido \n recuerde no puede ser negativo")
        else:
            break 
    salario_proporcional=(salario_mensual*dias_trabajados)/30
    salario_devengado=salario_proporcional+bonos
    salario_neto=salario_devengado*0.83-otras_deducciones    
if salario_mensual==0:
    print("sin trabajadores")
else:   
    print("el salario neto es ",salario_neto)
    