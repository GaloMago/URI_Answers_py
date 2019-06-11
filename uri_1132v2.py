def main():

    # entrada
    x = int(input())
    y = int(input())
    maior = 0
    menor = 0
    soma = 0

    # processamento
    if x > y:
        maior = x
        menor = y
    else:
        maior = y
        menor = x

    while menor <= maior:
        if menor % 13 != 0:
            soma += menor
        menor +=1
    # saida
    print(soma)

if __name__ == '__main__':
    main()