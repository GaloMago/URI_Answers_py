def main():

    # entrada
    n = int(input())


    contador = 1
    while contador < 11:
        tabua = n * contador
        print('%d x %d = %d' % (contador, n, tabua))
        contador +=1


if __name__ == '__main__':
    main()