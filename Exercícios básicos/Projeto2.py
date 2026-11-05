#Sistema te diz se o dia da semana é útil pelo número

num = int(input("Escreva um valor: "))

match num:
    case 1 | 7:
        print("Fim de semana")
    case 2 | 3 | 4 | 5 | 6:
        print("Dia útil")
    case _: 
        print("Opção inválida")
