matriz = [[ 0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]

print('Posições dos numeros')
print('')
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{l}, {c}]', end='')
    print()
print(' ')
print(" ")
for l in range(0, 3):
    pessoas = 0
    for c in range(0, 3):
        pessoas +=1
        matriz[l][c] = int(input(f'Digite o numero da posição [{l}, {c}]: '))
print('-='*30)



def verificandoMaior(valorAtual, maiorValor):
    if valorAtual >maiorValor:
        maiorValor = valorAtual
    return maiorValor

def tabelaDeJogos():
    linhas = len(matriz) 
    colunas = len(matriz[0]) 
    for l in range(0, linhas):
        for c in range(0, colunas):
            print(f'[{matriz[l][c]:^13}]', end='')
        print()
# Verificando se pe um quadrado magico

primeiraLinha = 0 
segundaLinha = 0
terceiraLinha = 0

primeiraConluna = 0
segundaConluna = 0
terceiraCOnluna = 0

primeiraDiagonal = 0
segundaLinhaDiagonal = 0

rangeFor = [0, 1, 2]
gambiarra = rangeFor[:]
gambiarra.sort(reverse=True)

maiorValor = 0
teste = 0

for m in rangeFor:
    primeiraLinha += matriz[0][m] 
    maiorValor = verificandoMaior(primeiraLinha, maiorValor)

    segundaLinha += matriz[1][m]
    maiorValor = verificandoMaior(segundaLinha, maiorValor)

    terceiraLinha += matriz[2][m]
    maiorValor = verificandoMaior(terceiraLinha, maiorValor)

    primeiraConluna += matriz[m][0]
    maiorValor = verificandoMaior(primeiraConluna, maiorValor)

    segundaConluna += matriz[m][1]
    maiorValor = verificandoMaior(segundaConluna, maiorValor)
    

    terceiraCOnluna += matriz[m][2]
    maiorValor =verificandoMaior(terceiraCOnluna, maiorValor)
    
    primeiraDiagonal += matriz[m][m]
    maiorValor = verificandoMaior(primeiraDiagonal, maiorValor)

    segundaLinhaDiagonal += matriz[m][gambiarra[m]]
    maiorValor = verificandoMaior(segundaLinhaDiagonal, maiorValor)

tabelaDeJogos()

print(f'O maior valor é {maiorValor}')
