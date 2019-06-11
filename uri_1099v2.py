def main():

    # entrada
    entradas = int(input())
    maior = 0
    menor = 0

    # processamento
    while entradas > 0:
        soma = 0
        x, y = map(int, input().split())

        if x > y:
            maior = x
            menor = y

        else:
            maior = y
            menor = x

        menor +=1
        while menor < maior:
            if menor % 2 != 0:
                soma += menor
            menor +=1 # convergência

        # saida
        print(soma)
        entradas -=1 # convergência

if __name__ == '__main__':
    main()