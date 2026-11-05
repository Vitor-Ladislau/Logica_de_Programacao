#O sistema vai te dar a média dos números pares digitados

i = 0
somaPar = 0
num = int(input("Escreva um número ou Digite 0 para encerrar o proceso: "))

while num != 0:
    if num % 2 == 0:
        somaPar = somaPar + num
        i = i + 1

    num = int(input("Escreva outro número ou Digite 0 para encerrar o proceso: "))

if i > 0:
    media = somaPar / i
    print("A média dos números pares digitados é: ", media)
else:
    print("Nenhum número par foi escrito")