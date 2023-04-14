hora_inicial = int(input("Digite a hora inicial = "))
minuto_inicial = int(input("Digite o minuto inicial = "))
hora_final = int(input("Digite a hora final = "))
minuto_final = int(input("Digite o minuto final = "))
hora_inicial_transcorrido = hora_inicial*60 + minuto_inicial
hora_final_transcorrido = hora_final*60 + minuto_final
diferenca = hora_final_transcorrido - hora_inicial_transcorrido
print("Minutos transcorridos = ", diferenca)

""" algoritmo não autoral """