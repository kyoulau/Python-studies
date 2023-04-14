valor_ingresso = float(input("Digite o valor do ingresso = "))
numero_ingressos = int(input("Digite o número de ingressos = "))
desconto = float(input("Digite seu desconto = "))
valor_estacionamento = float(input("Digite o valor estacionamento = "))
valor_pagar = (valor_ingresso * numero_ingressos) - ((valor_ingresso *
numero_ingressos) * desconto)/100 - valor_estacionamento
print("Valor a pagar = ", valor_pagar)

""" algoritmo não autoral """