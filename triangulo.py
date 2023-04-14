""" Dados três valores A, B, C, verificar se eles podem ser os
comprimentos dos lados de um triângulo e, se forem, verificar se
compõem um triângulo equilátero, isósceles ou escaleno. Indicar
também se estes valores não formam um triângulo. """

comp_a = int(input("Defina o valor do comprimento A "))
comp_b = int(input("Defina o valor do comprimento B "))
comp_c = int(input("Defina o valor do comprimento C "))

if comp_a != comp_b and comp_b != comp_c and comp_a != comp_c:
    print("O triangulo será escaleno")
elif comp_a == comp_b and comp_b != comp_c and comp_a != comp_c:
    print("O triangulo será isósceles")
elif comp_a == comp_b and comp_b == comp_c and comp_a == comp_c:
    print(" O triangulo será equilatero !")
else:
    print("as larguras não formam um triangulo")

""" ladoA = int(input("Digite o lado A = "))
ladoB = int(input("Digite o lado B = "))
ladoC = int(input("Digite o lado C = "))
if (ladoA < (ladoB + ladoC)) and (ladoB < (ladoA + ladoC)) and (ladoC <
(ladoA + ladoB)):
if ((ladoA == ladoB) and (ladoB == ladoC)):
print("Triangulo Equilatero!")
elif (ladoA == ladoB) or (ladoB == ladoC) or (ladoA == ladoC):
print("Triangulo Isosceles!")
else:
print("Triangulo Escaleno!")
else:
print("Lados não formam um triangulo!") """