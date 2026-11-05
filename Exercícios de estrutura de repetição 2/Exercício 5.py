PaisA = 90000000
PaisB = 140000000
anos = 0

while PaisB > PaisA:
    PaisA = PaisA + (PaisA * 0.035)
    PaisB = PaisB + (PaisB * 0.01)
    anos += 1

print(f"{anos} Anos")