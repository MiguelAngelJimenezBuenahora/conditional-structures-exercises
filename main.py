#Escriba un programa que determine si un caracter ingresado es letra, número, o ninguno de los dos. En caso que sea letra, determine si es mayúscula o minúscula.

#Ingrese caracter: 9
#Es numero.

#Ingrese caracter: A
#Es letra mayúscula.

#Ingrese caracter: f
#Es letra minúscula.

#Ingrese caracter: #
#No es letra ni número.

character =input("Enter a character: ")
if character.isalpha(): #.isalpha is for check if the date is letter
    if character.isupper(): #.isupper if for check if the date letter is on upper
        typedate = "Upper"
    else:
        typedate = "minuscule"
    print(f"""The character '{character}' is a letter and is {typedate}""")
elif character.isdigit():   #Verify if the dare is type number
    print(f"""The character '{character}' is a number""")
else: #any of two
    print(f"""The character '{character}' isn't letter or number.""")