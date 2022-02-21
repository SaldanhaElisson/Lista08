
numero1 = 1
numero2 = 0
numero3 = 0

print("QUESTÃO 1 ")
print("")
for n in range(0,12):
    numero3 = numero1 + numero2
    print(f'{numero3}, ', end="")
    numero1 = numero2
    numero2 = numero3