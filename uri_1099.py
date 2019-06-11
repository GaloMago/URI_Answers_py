def main():
    #entrada
    N = int(input())

    #processmento
    for i in range (N):
        soma = 0
        lista = [int(num) for num in input().split()]
        X = min(lista)
        Y = max(lista)

        for j in range(X+1, Y):
            if j % 2 !=0:
                soma += j
        #saida
        print(soma)

if __name__ == '__main__':
    main()