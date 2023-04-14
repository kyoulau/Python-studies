preco = float(input("Digite o valor da compra: "))
print("1. dinheiro\n 2. a vista no cartão\n 3.parcelado")
opcao = int(input("Escolha a forma de pagamento: "))

if(opcao == 1):
    calculo = preco * 0.90
    print(f"Preço final será {calculo}")
elif(opcao == 2):
    calculo = preco * 0.95
    print(f"Preço final será {calculo}")
elif(opcao == 3):
    print(f"Preço final será {preco}")
else:
    print("opção inválida !")