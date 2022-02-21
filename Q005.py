
matriz = []

for n in range(0, 2):
    matrizaux = []

    nome = input(f'Digite o nome do {n + 1}° competidor: ')

    matrizaux.append(nome)
    
    for i in range(0, 3):
        tempo = float(input(f'Digite o tempo da {i + 1}° volta: '))
        matrizaux.append(tempo)
    matriz.append(matrizaux)

def encontrar(elemento, lista):
    pos_i = 0 # variável provisória de índice
    pos_j = 0 # idem
    # print(lista)

    for i in range (0, 2): # procurar em todas as listas internas
        for j in range (0, 3): # procurar em todos os elementos nessa lista
            # print(j)
            # print(elemento)
            # print(lista[i][j])
            if elemento == lista[i][j]: # se encontrarmos elemento ('ana')
                print(lista[i][j])
                pos_i = i # guardamos o índice i
                pos_j = j # e o índice j
                return [pos_j, pos_i] # e retornamos os índices

         

maiorValor = 1000000

medias = []
voltar = 0

## saber qual foi o melhor temo
for n in range(0, 2):
    for  m in range(1, 3):
        # print(matriz[n][m])
        if matriz[n][m] < maiorValor:
            maiorValor =  matriz[n][m]
            # voltar = m + 1

## calculando media
for n in range(0, 2):
    aux = 0
    for  m in range(1, 3):
        aux = aux + matriz[n][m]
        medias.append(aux/3)

position = encontrar(maiorValor, matriz)
# print(position)
# print(matriz)

# competidor = position[0]
# print(competidor)

coluna = position[0]
linha  = position[1]

print("=" * 80)
print('ATIVIDADE 6 ITEM A')
print(f'Quem pecorreu o menor tempo foi: {matriz[linha][0]}')




