#Vai te dar a tabuada do número que o usuário pedir
#E vai multiplicar pelo outro número que o usuário pedir

num = int(input("Escreva o número que você deseja que seja escrito: "))
tabuada = int(input("Digite até qual número deseja saber a tabuada: "))

for contador in range (tabuada): 
    print (num, "*", contador + 1, "=", num * (contador + 1))