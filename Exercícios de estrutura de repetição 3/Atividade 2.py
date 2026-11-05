Homens = 0
Mulheres = 0
Sex = 0
Nom = 0
while Sex < 56 and Nom < 56:
    Sex +=1
    Nom +=1
    Sexo = int(input("Digite 1 se você é homem e 2 se você é mulher:  "))
    Nome = str(input("Digite seu Nome: "))
    if Sexo == 1:
        Homens +=1
    elif Sexo == 2:
        Mulheres +=1
    else:
        print("Você digitou um número inválido!")
print(f"Foram registrados {Homens} homens e {Mulheres} Mulheres!")