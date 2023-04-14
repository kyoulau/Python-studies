qtd_copias = int(input("Quantas cópias voce quer imprimir ? "))
custo_copia = 2.50
preco_total = qtd_copias * custo_copia
print("O custo total das cópias será de ", preco_total)
if (preco_total):
    print("Foram impressas",qtd_copias, "cópias" " no preço de ",preco_total)
    print("Cada copia custou ", qtd_copias/custo_copia)
