#Média aritmética
#O sistema lê três notas e calcule a média

somaNota = 0.0
quantidadeNota = int(input("Quantas notas serão digitadas: "))
for contador in range (quantidadeNota):
    nota = float(input("Digite a nota: "))
    somaNota =+ nota
media = somaNota / 4
print("Sua média é: ", media )