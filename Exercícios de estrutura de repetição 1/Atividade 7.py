contador = 0
somaPos = 0

while True:
    num = float(input("Escreva outro número ou Digite um número negativo para encerrar o proceso e mostrar a média: "))
    if num < 0:
        break
    somaPos += num
    contador += 1
if contador > 0: 
     media = somaPos / contador
     print("A média dos números pares digitados é: ", media)
else:
     print("Nenhum número positivo foi escrito, méia indefinida") 