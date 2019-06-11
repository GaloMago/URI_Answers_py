def main():

    contador = 0
    for i in range(5):
        #entrada
        valor = int(input())
        if valor % 2 == 0:
            contador += 1
    print("%d valores pares" %contador)


if __name__ == '__main__':
    main()