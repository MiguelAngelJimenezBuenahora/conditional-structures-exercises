#El riesgo de que una persona sufra enfermedades coronarias depende de su edad y su índice de masa corporal:

#      	edad < 45 	edad ≥ 45
#    IMC < 22.0 	bajo 	medio
#    IMC ≥ 22.0 	medio 	alto

#El índice de masa corporal es el cuociente entre el peso del individuo en kilos y el cuadrado de su estatura en metros.

#Escriba un programa que reciba como entrada la estatura, el peso y la edad de una persona, y le entregue su condición de riesgo.

age = int(input("""This program calculate your IMC and say you the level of warning to coronary heart diseases
Please insert your age: """))
Height = float(input("Plase insert your height on m: "))
Weight = float(input("Please insert your weight on kg: "))
imc = Weight/Height
if age < 45:
    if imc < 22:
        print("Your risk is low")
    elif imc >= 22:
        if imc <30:
             print("Your risk i medium")
        else:
            print("Your risk is high")
    elif age >=45:
        if imc < 22:
            print("Your risk i medium")
        elif imc >= 22:
            if imc < 30:
                print("Your risk is high")
            else:
                print("Your risk is so dangerous")