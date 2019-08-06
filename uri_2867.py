def main():

    # entrada
    casos = int(input())

    # processamento e saida
    for i in range(casos):
        n,m = map(int,input().split())
        expo = n ** m
        tam = len(str(expo))
        print(tam)


if __name__ == '__main__':
    main()