#Este programa calcula el total de lozas o baldosas que necesitas para tu piso de cualquier edificios 

## Todas mis variables de entradas 

Largo=float(input("Entre el largo de tu espacio en pies cuadrado"))
Ancho=float(input("Entre el ancho de tu espacio en pies cuadrado"))
LargoL=float(input("Entre el largo en pulgadas de la loza"))
AnchoL=float(input("Entre el ancho en pulgadas de la loza"))

##Todos los calculos

Area=(Largo*Ancho)
AreaL=(LargoL*AnchoL)
AreapiesL=(AreaL/144)
Areacalculada=(Area/AreapiesL)

##Todos mis resultados

print("El largo en pies " ,Largo)
print("El ancho en pies " ,Ancho)
print("Area del espacio calculada en pies " ,Area)
print("El area calculada de la loza en pies " ,AreapiesL)
print("Su total calculado de lozas son " ,Areacalculada)