def main():

    # entrada
    entrada = int(input())
    vezes = entrada * 4
    cont = 1
    pum = 'PUM'

    # processamento e saida
    while cont <= vezes:
        if cont % 4 == 0:
            print(pum, end='\n')
        else:
            print(cont,end=' ')
        cont +=1

if __name__ == '__main__':
    main()