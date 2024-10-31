#Escriba un programa que entregue la edad del usuario a partir de su fecha de nacimiento:

#Ingrese su fecha de nacimiento.
#Dia: 14
#Mes: 6
#Anno: 1948
#Usted tiene 62 annos

#Por supuesto, el resultado entregado depende del día en que su programa será ejecutado.

#Para obtener la fecha actual, puede hacerlo usando la función localtime que viene en el módulo time. Los valores se obtienen de la siguiente manera (suponiendo que hoy es 11 de marzo de 2011):

#>>> from time import localtime
#>>> t = localtime()
#>>> t.tm_mday
#11
#>>> t.tm_mon
#3
#>>> t.tm_year
#2011

#El programa debe tener en cuenta si el cumpleaños ingresado ya pasó durante este año, o si todavía no ocurre.

import time
#In case do you want use this code with the date of system, 
#you can use:
date_current = time.localtime()
anio_exercise = date_current.tm_year
month_exercise = date_current.tm_mon
day_exercise = date_current.tm_mday


#anio_exercise = 2011
#month_exercise = 3
#day_exercise = 11


dateofborn = input("""This program process your age of born and say you what is your age, 
Please can you insert you borntime in this format (dd/mm/aaaa): """)

#I'll Convert string to a date object

day, month, anio = map(int, dateofborn.split('/')) 

yearfromborntocurrent = anio_exercise - anio

if anio_exercise == anio:
    if (month_exercise, day_exercise) < (month, day):
        yearfromborntocurrent -= 1
print(f"""Your have {yearfromborntocurrent} annos""") 
