def main():

    while True:
        try:
            # entrada
            tam = int(input())
            matriz = criar_matriz(tam,tam)
            matriz123 = matriz_123(matriz)
            mostrar_matriz_1534(matriz123)

        except EOFError:
            break

def matriz_123(matriz):
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if i + j == len(matriz) - 1:  # observe a matriz 4x4 do exemplo
                matriz[i][j] = 2
            elif j == i:  # a diagonal principal sempre será 1
                matriz[i][j] = 1
            else:
                matriz[i][j] = 3
    return  matriz

def criar_matriz(li, co):
    vetor = [0] * li  # criação da 1º dimensão

    for i in range(len(vetor)):
        vetor[i] = [0] * co  # a cada volta, criará uma coluna

    return vetor

def mostrar_matriz_1534(matriz):
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            print(matriz[i][j],end='')
        print()


if __name__ == '__main__':
    main()