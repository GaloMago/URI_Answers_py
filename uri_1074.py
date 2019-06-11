def main():

    # entrada
    entradas = int(input())
    contador = 0

    # processamento
    while contador < entradas:
        numero = int(input())
        contador +=1

        if numero > 0 and numero % 2 == 0:
            print('EVEN POSITIVE')

        elif numero > 0 and numero % 2 != 0:
            print('ODD POSITIVE')

        elif numero < 0 and numero % 2 == 0:
            print('EVEN NEGATIVE')

        elif numero < 0 and numero % 2 != 0:
            print('ODD NEGATIVE')

        else:
            print('NULL')

if __name__ == '__main__':
    main()