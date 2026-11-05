J1 = 0
J2 = 0
points = 0

while J1 < 21 and J2 < 21 or points >= 2:
    vitoria = int(input("Digite quem ganhou: "))

    if vitoria ==1:
        J1 += 1
    elif vitoria ==2:
        J2 += 1

if J1 >= 21:
    print("Jogador 1 ganhou")
else:
    print("Jogador 2 ganhou")