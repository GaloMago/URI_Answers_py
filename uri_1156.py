def main():

    # entrada
    div = 1
    den = 1
    s = 0

    # processamento e saida
    while den <= 39:
        s += den / div
        den +=2
        div *=2
    print('%.2f'%s)


if __name__ == '__main__':
    main()