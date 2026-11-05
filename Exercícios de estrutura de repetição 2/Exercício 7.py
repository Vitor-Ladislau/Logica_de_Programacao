canal4 = 0
canal5 = 0
canal7 = 0
canal12 = 0
num = 1

total = 0

while num != 0:
    num = int(input("Digite o número do canal: "))

    if num ==  0:
        break

    pessoas = int(input("Digite o número de pessoas assistindo:"))
    total = total + pessoas


    if num == 4:
        canal4 += pessoas
    elif num == 5:
        canal5 += pessoas
    elif num == 7:
        canal7 += pessoas
    elif num == 12:
        canal12 += pessoas

if total > 0:
    Percent4 = (canal4/total)*100
    Percent5 = (canal5/total)*100
    Percent7 = (canal7/total)*100
    Percent12 = (canal12/total)*100

    print(f"{Percent4}% dos cidadões estão assistindo este canal.")
    print(f"{Percent5}% dos cidadões estão assistindo este canal.")
    print(f"{Percent7}% dos cidadões estão assistindo este canal.")
    print(f"{Percent12}% dos cidadões estão assistindo este canal.")
else:
    print("Nenhuma audiência registrada.")
