def main():

    # entrada
    cont = 0
    media = 0
    soma = 0

    # processamento
    while cont < 2:
        nota = float(input()) # entrada
        if 0 <= nota <= 10:
            soma += nota
            cont +=1
        else:
            print('nota invalida')
    media = soma / 2

    # saida
    print('media = %.2f'%(media))

    # loop
    while True:
        print('novo calculo (1-sim 2-nao)')
        res = int(input())
        if res == 1:
            return main()
        elif res == 2:
            break

if __name__ == '__main__':
    main()