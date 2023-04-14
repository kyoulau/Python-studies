""" ) Implemente um programa em Python para ler do teclado a
nota de um aluno. Verificar se o valor lido é uma nota válida. Se
não for, ler este valor até que a mesma seja válida.
 """

nota = float(input("Digite sua nota(entre 0 e 10) "))
while nota < 0 or nota > 10:
    print("Digite sua nota com valor válido (entre 0 e 10)")
    nota = float(input("Digite sua nota(entre 0 e 10) "))
if nota > 0 and nota < 11:
    print("Nota valida")
