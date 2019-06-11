def main():

    # entrada
    n = int(input())
    contador = 1
    quadrado = 0

    #processamento
    while contador <= n:
        if contador % 2 == 0:
            quadrado = contador ** 2
            print('%d^2 = %d'%(contador,quadrado))

        contador +=1
if __name__ == '__main__':
    main()