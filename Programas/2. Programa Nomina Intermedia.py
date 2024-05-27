'''
En este programa se utiliza varios conceptos, pero mas avanzados es importante tener en cuenta que establecemos una condicion
if y else donde establece que si el tiempo es menor de 40 en una semana el pago seria a tiempo normal, de lo contrario seria
a tiempo extra.
'''
Tiempo=int(input("Entra las horas trabajadas de la semana"))
Pago=int(input("Entra el pago por horas establecido"))

if Tiempo<40:
    Total=(Tiempo*Pago)
    print("Tu pago total es de" , Total)
else:
    Totalextra=((Tiempo-40)*Pago*1.5)+(40*Pago)
    print("Tu pago total a tiempo extra es de" , Totalextra)


