#Para corregir este desfase, en el año 1582 el papa Gregorio XIII introdujo un nuevo calendario, en el que el último año de cada siglo dejaba de ser bisiesto, a no ser que fuera divisible por 400.

#Escriba un programa que indique si un año es bisiesto o no, teniendo en cuenta cuál era el calendario vigente en ese año:

#Ingrese un anno: 1988
#1988 es bisiesto x

#Ingrese un anno: 2011
#2011 no es bisiesto  t

#Ingrese un anno: 1700
#1700 no es bisiesto

#Ingrese un anno: 1500
#1500 es bisiesto

#Ingrese un anno: 2400
#2400 es bisiesto

orbEarth = 365.25   #Number of days to earth rotate around the sun

yearnumber = int(input("Please insert a year number: "))

def isleap(yearnumber):
    if yearnumber < 1582:
        # Rule of juliano Calendary
        return yearnumber % 4 == 0
    else:
        # Rule of gregoriano calendary
        if yearnumber % 400 == 0:   #is leap year
            return True
        elif yearnumber % 100 == 0: #isn't leap year
            return False
        elif yearnumber % 4 == 0:   #is leap year
            return True
        else:
            return False
if isleap(yearnumber) == True:
    print(f"""{yearnumber} is a leap year""")
else:
    print(f"""{yearnumber} is'nt a leap year""")
    
    