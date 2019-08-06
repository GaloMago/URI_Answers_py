def main():

    # entrada
    termos = int(input())
    cont = 0
    t1 = 0
    t2 = 1

    # processamento e saida
    while cont < termos:
        if termos == 1:
            print(t1,end='')
            cont +=1
        else:
            print(t1,end=' ')
            t3 = t1 + t2
            t1 = t2
            t2 = t3
            cont +=1
            if cont + 1 == termos:
                print(t1,end='')
                break

if __name__ == '__main__':
    main()