
matriz = []
for n in range(0, 3):
    matrizaux = []

    nome = input(f'Digite o nome do aluno:  ')
    matrizaux.append(nome)  
    for i in range(0, 2):
        tempo = float(input(f'Digite a{i + 1}° nota: '))
        matrizaux.append(tempo)
    matriz.append(matrizaux)

medias = []
## calcular media
for n in range(0, 3):
    for i in range(0, 3):
        print(f'[{matriz[n][i]:^13}]', end='')
    print()

