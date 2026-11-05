preço = float(input("Digite o preço do carro: "))

avista = int(input("O pagamento será a vista?\n1- Sim\n2- Não\nDigite sua resposta: "))
if avista == 1:
    print(f"O valor do carro é R${preço}")
else:
    parcela = int(input(" Digite a quantidade de parcelas: 6, 12, 18, 24, 30, 36, 42, 48, 54, 60\nDigite a quantia desejada: "))
    if parcela == 6:
        preço = preço + (preço * 0.03)
        print(f"O valor do carro é R${preço}")
    elif parcela == 12:
        preço = preço + (preço * 0.06)
        print(f"O valor do carro é R${preço}")
    elif parcela == 18:
        preço = preço + (preço * 0.09)
        print(f"O valor do carro é R${preço}")
    elif parcela == 24:
        preço = preço + (preço * 0.12)
        print(f"O valor do carro é R${preço}")
    elif parcela == 30:
        preço = preço + (preço * 0.15)
        print(f"O valor do carro é R${preço}")
    elif parcela == 36:
        preço = preço + (preço * 0.18)
        print(f"O valor do carro é R${preço}")
    elif parcela == 42:
        preço = preço + (preço * 0.21)
        print(f"O valor do carro é R${preço}")
    elif parcela == 48:
        preço = preço + (preço * 0.24)
        print(f"O valor do carro é R${preço}")
    elif parcela == 54:
        preço = preço + (preço * 0.27)
        print(f"O valor do carro é R${preço}")
    elif parcela == 60:
        preço = preço + (preço * 0.30)
        print(f"O valor do carro é R${preço}")