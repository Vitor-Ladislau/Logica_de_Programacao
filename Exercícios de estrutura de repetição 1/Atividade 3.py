#O sistema vai dizer quantos números positivos e negativos foram escritos

NumNeg = 0
NumPos = 0
num = int(input("Digite um número inteiro para iniciar o programa e digite 0 para encerrar: "))

while num != 0:
    if num < 0:
        NumNeg = NumNeg + 1
    elif num > 0:
        NumPos = NumPos + 1

    num = int(input("Digite outro número ou digite 0 para encerrar o programa: "))

print(f"Você digitou {NumNeg} número(s) negativos e {NumPos} número(s) positivos")
  