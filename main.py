#Los tres lados a, b y c de un triángulo deben satisfacer la desigualdad triangular: cada uno de los lados no puede ser más largo que la suma de los otros dos.

#Escriba un programa que reciba como entrada los tres lados de un triángulo, e indique:

#    si acaso el triángulo es inválido; y
#    si no lo es, qué tipo de triángulo es.

#ngrese a: 3.9
#Ingrese b: 6.0
#Ingrese c: 1.2
#No es un triangulo valido.

#Ingrese a: 1.9
#Ingrese b: 2
#Ingrese c: 2
#El triangulo es isoceles.

#El triangulo es escaleno.
#Ingrese a: 3.0
#Ingrese b: 5.0
#Ingrese c: 4.0

def typeoftriangle(a, b, c):
    # Verify the triangular inequality
    if a + b > c and a + c > b and b + c > a:
        # Valid triangle, determine type
        if a == b == c:
            return "The triangle is equilateral."
        elif a == b or a == c or b == c:
            return "The triangle is isosceles."
        else:
            return "The triangle is scalene."
    else:
        return "The triangle is invalid."


a = float(input("Please inset the lenght of the face a to triangle: "))
b = float(input("Please inset the lenght of the face b to triangle: "))
c = float(input("Please inset the lenght of the face c to triangle: "))

result = typeoftriangle(a, b, c)
print(result)