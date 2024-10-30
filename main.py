#Escriba un programa que determine si el número entero ingresado por el usuario es par o no.

#Ingrese un número: 4
#Su número es par

#Ingrese un número: 3
#Su número es impar

number=int(input("Please insert a number int: "))

if number%2 ==0:
    print("The number is a par number")
elif number%2 >=0:
    print("the number is a odd numer")