def main():

    # entrada
    while True:
        m, n = map(int, input().split())
        auxtxt = ''
        maior = 0
        menor = 0
        soma = 0

    # processamento
        if m <= 0 or n <= 0:
            break

        if m > n:
            maior = m
            menor = n
        else:
            maior = n
            menor = m

        while menor <= maior:
            menor = str(menor)
            auxtxt += menor + ' '
            menor = int(menor)
            soma += menor
            menor += 1

        # saida
        print('{}Sum={}'.format(auxtxt,soma))

if __name__ == '__main__':
    main()