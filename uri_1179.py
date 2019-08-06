def main():

    # entrada
    pares = [0] * 5
    impares = [0] * 5

    for i in range(15):
        valor = int(input())
        if valor % 2 == 0:
            pares[i] = valor
            print(pares[i])
        else:
            impares[i] = valor
            print(impares[i])


if __name__ == '__main__':
    main()