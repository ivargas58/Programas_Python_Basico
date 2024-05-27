#Este programa calcula secuencias numericas o geometricas
selecion= int(input("Escriba el numero 1 para entrar a la secuencia numerica si no marque el 0 "))
if selecion >0:
    a1= int(input("Entre el valor incial de la serie "))
    n=int(input("Entre la cantidad de valores de la secuencia"))
    d=int(input("Entre la diferencia de la secuencia "))
    an=a1+(n-1)*d
    def serienumeric(n):
        aa1=a1
        lista = []
        while aa1<=n:
            lista.append(aa1)
            aa1+=d
        return lista
    sn=(n/2)*(a1+an)
    print ("El valor incial de la serie " ,a1)
    print ("El valor de diferencia " ,d)
    print ("El valor de al que quieres que llegue ",n)
    print ("Su valor final " ,an)
    print ("Su la sumatoria de la serie " ,sn)
    print (serienumeric(an))
else:
    a1=int(input("Valor inicial de la secuencia "))
    n=int(input("La cantidad de valores de la secuencia "))
    r=int(input("La razon de la secuencia "))
    an=a1*(r**(n-1))
    def secuencia_geometrica(n):
        aa1=a1
        lista = []
        while aa1<=n:
            lista.append (aa1)
            aa1*=r
        return lista
    sn=(a1)*(r**(n-1))/(n-1)
    print ("El valor incial de la serie " ,a1)
    print ("El valor de diferencia " ,r)
    print ("El valor de al que quieres que llegue ",n)
    print ("Su valor final " ,an)
    print ("Su la sumatoria de la serie " ,sn)
    print(secuencia_geometrica(an))
