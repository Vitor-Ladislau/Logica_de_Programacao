Compras = 0
Comprastotal = 0
Comprasvista = 0
Comprasprazo = 0
Valorvista = 0
Valorprazo = 0

while Compras < 15:
    Compras +=1
    Pagamento = int(input("Digite o modelo de pagamento 1 para à vista e 2 para a prazo: "))
    compra = float(input("Digite o valor da sua compras: "))
    if Pagamento == 1:
        Comprasvista +=1
        Valorvista += compra
        Comprastotal += compra
    elif Pagamento == 2:
        Comprasprazo +=1
        Valorprazo += compra
        Parcela1 = compra/3
        Comprastotal += compra
        print(f"A primeira prestação de sua compra sai no valor de R${Parcela1}")
    elif Pagamento > 2 or Pagamento < 1:
        print("Método de pagamento inválido!")

print(f"Total compras a vista {Valorvista}")
print(f"Total compra a prazo {Valorprazo}")
print(f"Valor total {Comprastotal}")
