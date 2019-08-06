def main():

    # entrada
    while True:
        ordem = int(input())
        if ordem == 0:
            return False
        matriz = criar_matriz(ordem,ordem)
        preencher_matriz_1435(matriz,1)
        mostrar_matriz(matriz)
        print(no_centro_matriz(matriz))

def mostrar_matriz(matriz):
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            print(matriz[i][j],end=' ')
        print()

def preencher_matriz_1435(matriz,ordem):
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if no_centro_matriz(matriz):
                matriz[i][j] += 1
            else:
                matriz[i][j] = ordem

def criar_matriz(li,co):
    vetor = [0] * li #criação da 1º dimensão

    for i in range (len(vetor)):
        vetor[i] = [0] * co # a cada volta, criará uma coluna

    return vetor

def no_centro_matriz(matriz):
    contador = 0
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if i == j:
                contador +=1
    return matriz[contador-1][contador-1]

if __name__ == '__main__':
    main()