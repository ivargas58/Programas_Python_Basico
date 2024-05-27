#Este programa determina si tu numero es par o impar
number=float(input("Escriba un numero"))
while number < 5:
    if number %2 == 0:
        print("El numero " ,str (number), "Es par")
    else:
        print("El numero" , str(number), "Es impar")
    number = number + 1
    