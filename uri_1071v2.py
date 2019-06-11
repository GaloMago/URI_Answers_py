def main():

    # entrada
    n1 = int(input())
    n2 = int(input())
    soma = 0
    maior = 0
    menor = 1

    if n1 > n2:
        maior = n1
        menor += n2
    elif n2 > n1:
        maior = n2
        menor += n1

    while menor < maior:
        if menor % 2 != 0:
            soma +=menor
        menor +=1
    print(soma)

if __name__ == '__main__':
    main()
