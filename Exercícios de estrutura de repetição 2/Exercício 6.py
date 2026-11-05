#np = Num par e nI = Numero impar

num = 1
totalP = 0
totalN = 0
nI = "0"
nP = "0"
nPos = 0
nNeg = 0
somaPos = 0
somaNeg = 0
somaTotal = 0

while num !=0:
    num = int(input("Digite um número: "))

    if num%2 == 0 and num!= 0:
        nP += str(num) + ", "
    elif num != 0:
        nI += str(num) + ", "
    if num > 0:
        nPos += 1
        somaPos += num
    elif num < 0:
        nNeg += 1
        somaNeg += num
somaTotal = somaNeg + somaPos

print(f"Os número impares são: {nI}")
print(f"Os número pares são: {nP}")
print(f"A soma dos números positivos são: {somaPos}")
print(f"A soma dos números negativos são: {somaNeg}")