from matrizesfun import *
def main():

    # entrada
    matriz = criar_matriz(12,12)
    opera = input()
    preencher_matriz(matriz)


    if opera == 'S':
        resultado = soma_area_superior(matriz)
    elif opera == 'M':
        resultado = media_area_superior(matriz)

    print('%.1f'%resultado)

if __name__ == '__main__':
    main()