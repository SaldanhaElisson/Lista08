from ssl import OPENSSL_VERSION_INFO


cedulasDisp = [2, 5, 10, 20, 50, 100, 200];

saque = int(input("Digite o dinheiro: "))
ceduldas = []
maiorCed = 200

while True:
    if saque >= 200:
        ceduldas.append("200")
        saque = saque - 200
    elif saque >= 100 and saque < 200:
        ceduldas.append("100")
        saque = saque - 100
    elif saque >= 50 and saque < 100:
        ceduldas.append("50")
        saque = saque - 50
    elif saque >= 20 and saque < 50:
        ceduldas.append("20")
        saque = saque - 20
    elif saque >= 10 and saque < 20:
        ceduldas.append("10")
        saque = saque - 10
    elif saque >= 5 and saque < 10:
        ceduldas.append("5")
        saque = saque - 5
    elif saque >= 2 and saque < 5:
        ceduldas.append("2")
        saque = saque - 2
    else:
        break


contador = " ".join(ceduldas)

# print(contador)

totcedWithValue = []

for n in range(0, len(ceduldas)):
    totCed =  contador.count(f'{ceduldas[n]}')
    aux = [totCed, ceduldas[n]]
    if aux in totcedWithValue:
        continue
    totcedWithValue.append(aux)

# print(totcedWithValue)

for n in range(0, len(totcedWithValue)):
    print(f'{totcedWithValue[n][0]} cedulas de {totcedWithValue[n][1]} reais')