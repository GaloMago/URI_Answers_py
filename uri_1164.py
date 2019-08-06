def main():

    # entrada
    casos = int(input())

    # processamento
    for i in range(casos):
        som_div = 0
        n = int(input())
        for d in range(1,n):
            if n % d == 0:
                som_div +=d

        # saidas
        if som_div == n:
            print('%d eh perfeito'%n)
        else:
            print('%d nao eh perfeito'%n)


if __name__ == '__main__':
    main()