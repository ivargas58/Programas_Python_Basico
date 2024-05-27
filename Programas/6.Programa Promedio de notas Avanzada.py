#Este programa te pide cuantas notas someteras y te calcula el total de tu promedio 
cantidad=int(input("Indique la cantidad de notas a promediar"))
suma=0
i=1
while(i<=cantidad):
    print("Indique la nota numero: ",i)
    nota=float(input())
    i+=1
    suma+=nota
    pro=suma/cantidad
print("El promedio de nota es " ,pro)
    