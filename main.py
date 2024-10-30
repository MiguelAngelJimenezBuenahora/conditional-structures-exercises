#Escriba un programa que reciba como entrada dos números, y los muestre ordenados de menor a mayor:

#Ingrese numero: 51
#Ingrese numero: 24
#24 51

numberoftwonumbers1= int(input(""""Hello user, this is a program to order form smallest to largest, 
Please can you insert a number: """))
numberoftwonumbers2= int(input("Please can you inset another number: "))

if numberoftwonumbers1 <= numberoftwonumbers2:
    smallestnumber1 = numberoftwonumbers1
    biggestnumber1 = numberoftwonumbers2
else:
    smallestnumber1 = numberoftwonumbers2
    biggestnumber1 = numberoftwonumbers1

print(f"""{smallestnumber1} {biggestnumber1}""")
#A continuación, escriba otro programa que haga lo mismo con tres números:
#Ingrese numero: 8
#Ingrese numero: 1
#Ingrese numero: 4
#1 4 8
numberofthreenumbers1 =int(input("""Now, for the next part, we doing the same but with three numbers
Please insert the first number: """))
numberofthreenumbers2 =int(input("Please insert the second number: "))
numberofthreenumbers3 =int(input("Please insert the third number: "))

if numberofthreenumbers1 <= numberofthreenumbers2 and numberoftwonumbers1 <= numberofthreenumbers3:
    smallestnumber2 = numberofthreenumbers1
    if numberofthreenumbers2 <= numberofthreenumbers3:
        mediumnumbers2 = numberofthreenumbers2
        biggestnumber2 = numberofthreenumbers3
    else:
        mediumnumbers2 = numberofthreenumbers3
        biggestnumber2 = numberofthreenumbers2
elif numberofthreenumbers2 <= numberofthreenumbers1 and numberofthreenumbers2 <= numberofthreenumbers3:
    smallestnumber2 = numberofthreenumbers2
    if numberofthreenumbers1 <= numberofthreenumbers3:
        mediumnumbers2 = numberofthreenumbers1
        biggestnumber2 = numberofthreenumbers3
    else:
        mediumnumbers2 = numberofthreenumbers3
        biggestnumber2 = numberofthreenumbers1
else:
    smallestnumber2 = numberofthreenumbers3
    if numberofthreenumbers1 <= numberofthreenumbers2:
        mediumnumbers2 = numberofthreenumbers1
        biggestnumber2 = numberofthreenumbers2
    else:
        mediumnumbers2 = numberofthreenumbers2
        biggestnumber2 = numberofthreenumbers1
print(f"""{smallestnumber2} {mediumnumbers2} {biggestnumber2}""")
#Finalmente, escriba un tercer programa que ordene cuatro números:

#Ingrese numero: 7
#Ingrese numero: 0
#Ingrese numero: 6
#Ingrese numero: 1
#0 1 6 7

#Recuerde que su programa debe entregar la solución correcta para cualquier combinación de números, no sólo para los ejemplos mostrados aquí.

#Hay más de una manera de resolver cada ejercicio.

numberoffourthnumbers1 =int(input("""Now, for the next part, we doing the same but with fourth numbers
Please insert the first number: """))
numberoffourthnumbers2 =int(input("Please insert the second number: "))
numberoffourthnumbers3 =int(input("Please insert the third number: "))
numberoffourthnumbers4 =int(input("Please insert the fourth number: "))

if numberoffourthnumbers1 <= numberoffourthnumbers2 and numberoffourthnumbers1 <= numberoffourthnumbers3 and numberoffourthnumbers1 <= numberoffourthnumbers4:
    smallestnumber3 = numberoffourthnumbers1
    if numberoffourthnumbers2 <= numberoffourthnumbers3 and numberoffourthnumbers2 <= numberoffourthnumbers4:
        mediumnumbers3_1 = numberoffourthnumbers2
        if numberoffourthnumbers3 <= numberoffourthnumbers4:
            mediumnumbers3_2 = numberoffourthnumbers3
            biggestnumber3 = numberoffourthnumbers4
        else:
            mediumnumbers3_2 = numberoffourthnumbers4
            biggestnumber3 = numberoffourthnumbers3
    elif numberoffourthnumbers3 <= numberoffourthnumbers2 and numberoffourthnumbers3 <= numberoffourthnumbers4:
        medio1 = numberoffourthnumbers3
        if numberoffourthnumbers2 <= numberoffourthnumbers4:
            mediumnumbers3_2 = numberoffourthnumbers2
            biggestnumber3 = numberoffourthnumbers4
        else:
            mediumnumbers3_2 = numberoffourthnumbers4
            biggestnumber3 = numberoffourthnumbers2
    else:
        mediumnumbers3_1 = numberoffourthnumbers4
        if numberoffourthnumbers2 <= numberoffourthnumbers3:
            mediumnumbers3_2 = numberoffourthnumbers2
            biggestnumber3 = numberoffourthnumbers3
        else:
            mediumnumbers3_2 = numberoffourthnumbers3
            biggestnumber3 = numberoffourthnumbers2
elif numberoffourthnumbers2 <= numberoffourthnumbers1 and numberoffourthnumbers2 <= numberoffourthnumbers3 and numberoffourthnumbers2 <= numberoffourthnumbers4:
    smallestnumber3 = numberoffourthnumbers2
    if numberoffourthnumbers1 <= numberoffourthnumbers3 and numberoffourthnumbers1 <= numberoffourthnumbers4:
        mediumnumbers3_1 = numberoffourthnumbers1
        if numberoffourthnumbers3 <= numberoffourthnumbers4:
            mediumnumbers3_2 = numberoffourthnumbers3
            biggestnumber3 = numberoffourthnumbers4
        else:
            mediumnumbers3_2 = numberoffourthnumbers4
            biggestnumber3 = numberoffourthnumbers3
    elif numberoffourthnumbers3 <= numberoffourthnumbers1 and numberoffourthnumbers3 <= numberoffourthnumbers4:
        mediumnumbers3_1 = numberoffourthnumbers3
        if numberoffourthnumbers1 <= numberoffourthnumbers4:
            mediumnumbers3_2 = numberoffourthnumbers1
            biggestnumber3 = numberoffourthnumbers4
        else:
            mediumnumbers3_2 = numberoffourthnumbers4
            biggestnumber3 = numberoffourthnumbers1
    else:
        mediumnumbers3_1 = numberoffourthnumbers4
        if numberoffourthnumbers1 <= numberoffourthnumbers3:
            mediumnumbers3_2 = numberoffourthnumbers1
            biggestnumber3 = numberoffourthnumbers3
        else:
            mediumnumbers3_2 = numberoffourthnumbers3
            biggestnumber3 = numberoffourthnumbers1
elif numberoffourthnumbers3 <= numberoffourthnumbers1 and numberoffourthnumbers3 <= numberoffourthnumbers2 and numberoffourthnumbers3 <= numberoffourthnumbers4:
    smallestnumber3 = numberoffourthnumbers3
    if numberoffourthnumbers1 <= numberoffourthnumbers2 and numberoffourthnumbers1 <= numberoffourthnumbers4:
        mediumnumbers3_1 = numberoffourthnumbers1
        if numberoffourthnumbers2 <= numberoffourthnumbers4:
            mediumnumbers3_2 = numberoffourthnumbers2
            biggestnumber3 = numberoffourthnumbers4
        else:
            mediumnumbers3_2 = numberoffourthnumbers4
            biggestnumber3 = numberoffourthnumbers2
    elif numberoffourthnumbers2 <= numberoffourthnumbers1 and numberoffourthnumbers2 <= numberoffourthnumbers4:
        mediumnumbers3_1 = numberoffourthnumbers2
        if numberoffourthnumbers1 <= numberoffourthnumbers4:
            mediumnumbers3_2 = numberoffourthnumbers1
            biggestnumber3 = numberoffourthnumbers4
        else:
            mediumnumbers3_2 = numberoffourthnumbers4
            biggestnumber3 = numberoffourthnumbers1
    else:
        mediumnumbers3_1 = numberoffourthnumbers4
        if numberoffourthnumbers1 <= numberoffourthnumbers2:
            mediumnumbers3_2 = numberoffourthnumbers1
            biggestnumber3 = numberoffourthnumbers2
        else:
            mediumnumbers3_2 = numberoffourthnumbers2
            biggestnumber3 = numberoffourthnumbers1
else:
    smallestnumber3 = numberoffourthnumbers4
    if numberoffourthnumbers1 <= numberoffourthnumbers2 and numberoffourthnumbers1 <= numberoffourthnumbers3:
        mediumnumbers3_1 = numberoffourthnumbers1
        if numberoffourthnumbers2 <= numberoffourthnumbers3:
            mediumnumbers3_2 = numberoffourthnumbers2
            biggestnumber3 = numberoffourthnumbers3
        else:
            mediumnumbers3_2 = numberoffourthnumbers3
            biggestnumber3 = numberoffourthnumbers2
    elif numberoffourthnumbers2 <= numberoffourthnumbers1 and numberoffourthnumbers2 <= numberoffourthnumbers3:
        mediumnumbers3_1 = numberoffourthnumbers2
        if numberoffourthnumbers1 <= numberoffourthnumbers3:
            mediumnumbers3_2 = numberoffourthnumbers1
            biggestnumber3 = numberoffourthnumbers3
        else:
            mediumnumbers3_2 = numberoffourthnumbers3
            biggestnumber3 = numberoffourthnumbers1
    else:
        mediumnumbers3_1 = numberoffourthnumbers3
        if numberoffourthnumbers1 <= numberoffourthnumbers2:
            mediumnumbers3_2 = numberoffourthnumbers1
            biggestnumber3 = numberoffourthnumbers2
        else:
            mediumnumbers3_2 = numberoffourthnumbers2
            biggestnumber3 = numberoffourthnumbers1
print(f"""{smallestnumber3} {mediumnumbers3_1} {mediumnumbers3_2} {biggestnumber3}""")
