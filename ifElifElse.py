nota1 = float(input("digite a nota 1 = "))
nota2 = float(input("digite a nota 2 = "))
nota3 = float(input("digite a nota 3 = "))
nota4 = float(input("digite a nota 4 = "))
media = (nota1 + nota2 + nota3 + nota4)/4
print("Media = ", media)
if media >= 7:
    print("Aprovado")
else:
if media >= 4:
    print("Exame Final")

else:
    print("Reprovado")
