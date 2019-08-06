def main():

    # entrada
    while True:
        n = int(input())
        if n == 0:
            break
        matriz(n)
        print()

def matriz(n):
    matriz = [1]*n
    for i in range(n):
        matriz[i] = [1]*n

    aux = 1
    for i in range(len(matriz)):
        aux2 = aux
        for j in range(len(matriz)):
            matriz[i][j] = aux2
            aux2 *=2
        aux *=2
    mostrar(matriz,n)

def mostrar(matriz,n):
    width = len(str((2 ** (n - 1)) ** 2)) # justificar
    for i in range(len(matriz)):
        for j in range(len(matriz)):
            if j == len(matriz)-1:
                print('{:{}d}'.format(matriz[i][j], width))
            else:
                print('{:{}d} '.format(matriz[i][j], width), end='')

if __name__ == '__main__':
    main()
# https://www.portugal-a-programar.pt/forums/topic/75509-resolu%C3%A7%C3%A3o-uri-1557/