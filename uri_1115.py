def main():

    # entrada
    while True:
        x,y = map(int, input().split())

        # processamento
        if quadrante(x,y) == False:
            return False
        # saida
        print(quadrante(x,y))

def quadrante(x,y):

    if x > 0 and y > 0:
        return 'primeiro'

    elif x > 0 and y < 0:
        return 'quarto'

    elif x < 0 and y < 0:
        return 'terceiro'

    elif x < 0 and y > 0:
        return 'segundo'

    else:
        return False

if __name__ == '__main__':
    main()