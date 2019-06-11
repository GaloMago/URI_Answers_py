def main():
    # entrada
    maior = 0
    lista = {}
    posicao = 0

    # processamento
    while posicao < 6:
        valor = int(input())
        if (valor > maior):
            maior = valor
            lista[valor] = posicao
        posicao += 1

    # saida
    print(maior)
    print(lista[maior] + 1)


if __name__ == '__main__':
    main()