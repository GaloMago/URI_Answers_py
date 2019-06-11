def main():

    # entrada
    numero = float(input())

    # processamento e saida
    if 0 <= numero <= 25:
        print('Intervalo [0,25]')

    elif 25 < numero <= 50:
        print('Intervalo (25,50]')

    elif 50 < numero <= 75:
        print('Intervalo (50, 75]')

    elif 75 < numero <= 100:
        print('Intervalo (75,100]')

    else:
        print('Fora de intervalo')

if __name__ == '__main__':
    main()