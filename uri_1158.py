def main():

    # entrada
    casos = int(input())

    for i in range(casos):
        x,y = map(int,input().split())
        cont = x
        soma = 0
        while cont < y:
            if (x + cont) % 2 !=0:
                soma += (x + cont)
                cont +=1
            else:
                cont = cont
        print(soma)
if __name__ == '__main__':
    main()