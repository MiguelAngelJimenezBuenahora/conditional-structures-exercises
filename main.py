#Escriba un programa que pida al usuario dos palabras, y que indique cuál de ellas es la más larga y por cuántas letras lo es.

#Palabra 1: edificio
#Palabra 2: tren
#La palabra edificio tiene 4 letras mas que tren.

#Palabra 1: sol
#Palabra 2: paralelepipedo
#La palabra paralelepipedo tiene 11 letras mas que sol

#Palabra 1: plancha
#Palabra 2: lapices
#Las dos palabras tienen el mismo largo


# request two words to user
word1 = input("Introduce la primera palabra: ")
word2 = input("Introduce la segunda palabra: ")

# Calcute the lenght of both words
leng_word1 = len(word1)  #The sentence "len" is used for read the size of a date
leng_word2 = len(word2)


# Compare the lengths and determine which is longer
if leng_word1 > leng_word2:
    difference = leng_word1 - leng_word2
    print(f"La palabra más larga es '{word1}' con {difference} letras más que '{word2}'.")
elif leng_word2 > leng_word1:
    difference = leng_word2 - leng_word1
    print(f"La palabra más larga es '{word2}' con {difference} letras más que '{word1}'.")
else:
    print("Ambas palabras tienen la misma longitud.")

