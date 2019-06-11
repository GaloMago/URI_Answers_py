def main():

    # entrada
    x = int(input())
    y = int(input())
    maior = 0
    menor = 0
    resto = 0

    # processamento
    if x > y:
        maior = x
        menor = y
    else:
        maior = y
        menor = x

    menor +=1

    while menor < maior:
        if menor % 5 == 2 or menor % 5 == 3:
            # saida
            print(menor)
        menor +=1

if __name__ == '__main__':
    main()
