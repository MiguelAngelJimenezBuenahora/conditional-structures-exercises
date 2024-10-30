#Escriba un programa que pida dos números enteros y que calcule la división, indicando si la división es exacta o no.

#Dividendo: 14
#Divisor: 5

#La división no es exacta.
#Cociente: 2
#Resto: 4

#Dividendo: 100
#Divisor: 10

#La división es exacta.
#Cociente: 10
#Resto: 0

dividend = int(input("""Welcome to that program, this program say you if the division is an exact division or no:
                     please insert the dividend of division: """))
divider = int(input("please insert thte divider of division: "))
Restofdivision =dividend%divider    
quotient = dividend//divider
if Restofdivision <0:
        print("the division isn't exact")
elif Restofdivision >0:
        print("the division isn't exact")
else:
        print("the division is exact")
print(f"""quotient: {quotient}
rest: {Restofdivision}""")
    

