def main():

    # entrada
    matriz = criar_matriz(12,12)
    opera = input()
    preencher_matriz(matriz)

    if opera == 'S':
        soma = 0
        for i in range(len(matriz)):
            for j in range(len(matriz[i])):
                if i - j >= 1 and i + j < len(matriz) - 1:
                    soma += matriz[i][j]
        print('%.1f'%soma)

    else:
        contador = 0
        soma = 0
        for i in range(len(matriz)):
            for j in range(len(matriz[i])):
                if i - j >= 1 and i + j < len(matriz) - 1:
                    contador +=1
                    soma += matriz[i][j]
        print('%.1f'%(soma/contador))

def criar_matriz(li, co):
    vetor = [0] * li

    for i in range(len(vetor)):
            vetor[i] = [0] * co

    return vetor

def preencher_matriz(matriz):
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            matriz[i][j] = float(input())


if __name__ == '__main__':
    main()