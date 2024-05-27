'''
Este programa es un poco mas avanzado ya que da mas resultados que el anterior, pero sigue la misma logica
'''
Horas=int(input("Ingrese las horas trabajadas aqui"))
Pago=int(input("Ingrese el pago por hora aqui"))
if Horas>40:
        Bruto=((Horas-40)*Pago*1.5)+(40*Pago)
        DSS=(Bruto*.064)
        Dtax=(Bruto*.105)
        Neto=(Bruto-DSS-Dtax)
        print("Sus horas trabajadas" , Horas)
        print("Su pago por hora es" , Pago)
        print("Su ingreso bruto a tiempo extra es" , Bruto)
        print("Su descuento de Seguro Social", DSS)
        print("Su descuento de impuesto" , Dtax)
        print("Su ingreso neto a tiempo extra", Neto)
else:
        Bruto=(Horas*Pago)
        DSS=(Bruto*.062)
        Dtax=(Bruto*.105)
        Neto=(Bruto-DSS-Dtax)
        print("Sus horas trabajadas" , Horas)
        print("Su pago por hora es" , Pago)
        print("Su ingreso bruto es" , Bruto)
        print("Su descuento de Seguro Social", DSS)
        print("Su descuento de impuesto" , Dtax)
        print("Su ingreso neto", Neto)
    
