def main():

    # entrada
    matriz = criar_matriz(12,12)
    coluna = int(input())
    opera = input()
    preencher_matriz(matriz)
    print(in_linha_1182(opera,coluna,matriz))


def in_linha_1182(opera,coluna,matriz):
    soma = 0
    contador = 0
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if j == coluna:
                contador +=1
                soma += matriz[i][j]
    if opera == 'S':
        return soma
    else:
        return ('%.1f'%(soma/contador))

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