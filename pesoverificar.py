peso = float(input("Qual seu peso em kg ? "))
if peso < 50:
    print("Peso palha")
elif peso >= 50 and peso < 60:
    print("Peso pluma")
elif peso >= 60 and peso < 76:
    print("peso leve")
elif peso >= 75 and peso < 88:
    print("Peso pesado")
else:
    print("Super pesado")