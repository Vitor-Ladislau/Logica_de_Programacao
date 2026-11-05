cliente = 0

while cliente < 3:

    cliente +=1

    nome = str(input("Digite o nome do cliente: "))
    vcompra = float(input("Digite o valor da compra do cliente: "))


    if vcompra < 500000:
        print(nome, "Parabéns, você acaba de recerber um bônus de 10% em sua compra!")
    else:
        print(nome, "Parabéns, você acaba de recerber um bônus de 15% em sua compra!")

