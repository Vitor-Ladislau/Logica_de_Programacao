#O sistema vai subtrair 1 número do número digitado pelo usuário até chegar a 0

num1 = int(input("Digite um número: "))
num = 0

for contador in range(num1, num -1, - 1):
    print(contador)