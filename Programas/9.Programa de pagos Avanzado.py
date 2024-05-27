#Programa bancario 
p=float(input("Entre el pago inicial "))
r=float(input("Entre el interes en valor porcentual "))
n= float(input("Entre el cargo por termino "))
t=float(input('Entre el tiempo anual '))
r=r/100
a=(p)*(r/n)*(pow(1+r/n,n*t))/((pow(1+r/n,n*t))-1)
print('La cantidad principar es ',p)
print('El interes es de ',r)
print('Cargos por terminos es ',n)
print(' La cantidad de anual es ',t)
a=round(a,2)
print('Monto total por periodo ',a)
consulta= input('Escriba Si si quiere consultar otra vez sino escriba No ')
while consulta == 'Si':
    p=float(input("Entre el pago inicial "))
    r=float(input("Entre el interes en valor porcentual "))
    n= float(input("Entre el cargo por termino "))
    t=float(input('Entre el tiempo anual '))
    r=r/100
    a=(p)*(r/n)*(pow(1+r/n,n*t))/((pow(1+r/n,n*t))-1)
    print('La cantidad principar es ',p)
    print('El interes es de ',r)
    print('Cargos por terminos es ',n)
    print(' La cantidad de anual es ',t)
    a=round(a,2)
    print('Monto total por periodo ',a)
    consulta= input("Desea otra consulta?(Si o No) ")
else:
    print('Gracias por usar mi programa ;)')
    
   