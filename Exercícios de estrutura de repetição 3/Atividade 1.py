num = 0
num1 = 0

while num < 80:
    num +=1
    nume = int(input("Digite um número: "))
    if nume >= 10 and nume <=150:
        num1 +=1

print("Você digitou", num1, "número(s) maior ou igual a 10 e menor ou igual a 150!")
