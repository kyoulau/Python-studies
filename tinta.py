raio = float(input("Qual o valor do raio ? "))
altura = float(input("Qual é a altura ? "))
pi = 3.14
area_lateral = altura * (2 * pi * raio * altura)
area_base = (pi * raio * raio)
area_cilindro = area_base + area_lateral
total_litros = area_cilindro/3
custo = (total_litros/5)*50
print("o custo será de ", custo, "reais e ", total_litros, "latas")