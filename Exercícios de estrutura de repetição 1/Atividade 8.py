contador=0
NumPar=0
num = int(input("Digite um número inteiro positivo: "))
    
if num % 2 == 0: 
    for contador in range (num,0,-2):
        print(contador)
        
else:
    for contador in range(num-1,0,-2):
        print(contador) 
        

