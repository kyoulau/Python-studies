idade = int(input("Qual sua idade ? "))

if idade <16:
    print("Não pode votar. Não pode dirigir")
if idade >=16 and idade < 18:
    print("voce pode votar. não pode dirigir")
if idade >=18:
    print("Voce pode votar. Voce pode dirigir")