""" Implemente um programa em Python para imprimir na tela o
somatório dos 10 primeiros números inteiros a partir do 1. """
contador = 1
soma = 0 
while contador < 11:
    soma = contador + soma
    print(f"A soma é {soma}")
    contador = contador + 1
