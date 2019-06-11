def main():

    # entrada
    casos = int(input())
    cont = 1
    expo = 1
    aux = 0

    # processamento e saídas
    while cont <= casos:
        aux = cont ** expo
        print(aux,end=' ')
        expo +=1

        if expo == 3:
            aux = cont ** expo
            print(aux,end='\n')
            expo = 1
            cont +=1

if __name__ == '__main__':
    main()
