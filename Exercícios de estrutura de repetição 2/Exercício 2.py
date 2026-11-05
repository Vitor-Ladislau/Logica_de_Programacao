vestu = 0
naoPere = 0
pere = 0
higi = 0
limp = 0
prod = 1

while prod != 0:
    prod = int(input("Digite o código do produto (0 para sair): "))

    if prod == 1:
        naoPere += 1

    elif prod >= 2 and prod <=4 :
        pere += 1
    
    elif prod == 5 or prod == 6:
        vestu += 1
    
    elif prod == 7:
        higi += 1

    elif prod >= 8 and prod <= 15:
        limp += 1

    else: 
        print("Erro")

print("--- LISTA DE PRODUTOS ---")
print(f"Alimento não perecível = {naoPere}")
print(f"Alimento perecível = {pere}")
print(f"Vestuário = {vestu}")
print(f"higiente pessoal = {higi}")
print(f"Limpeza e utensílios domésticos = {limp}")
print("-------------------------")