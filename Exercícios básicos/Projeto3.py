#Sistema te diz se os 10 números que você digitar
#são par ou ímpar

Numeros = 0
for contador in range (10):
    Numero = int(input("Digite seu número: "))
    if Numero % 2 == 0 :
        print(Numero, "é um número Par")
    else:
        print("é um número Impar")