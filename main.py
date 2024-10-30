

#Escriba un programa que simule una calculadora básica, este puede realizar operación de suma, resta, multiplicación y división.

#El programa debe recibir como entrada 2 números reales y un operador, que puede ser +, -, * o /.

#La salida del programa debe ser el resultado de la operación.

#Operando: 3
#Operador: +
#Operando: 2
#3 + 2 = 5

#Operando: 6
#Operador: -
#Operando: 7
#6 - 7 = -1

#Operando: 4
#Operador: *
#Operando: 5
#4 * 5 = 20

#Operando: 10
#Operador: /
#Operando: 4
#10 / 4 = 2.5

#Operando: -1
#Operador: **
#Operando: 4
#-1 ** 4 = 1

number1 = float(input("""In this program you can input two number and insert a operator and solve the operation 
Please insert a number: """))
operator = input("Please insert the operator: ")
number2 = float(input("Please insert the other number: "))
if operator == '-':
    result = number1-number2
elif operator == '+':
    result = number1+number2
elif operator == 'x' or '*':
    result = number1*number2
elif operator == '/':
    if number2 !=0: #Verivy if doesn't 0 the number2
        result = number1/number2
    else:
        result ="Error, division on 0"
else:
    result = "Operator invalid"
print(f"""The result for operation between {number1} {operator} {number2} is: {result}""")

