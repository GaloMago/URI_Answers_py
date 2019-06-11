def main():

    # entrada
    casos = int(input())
    cont = 1
    expo = 1
    aux = 0

    # processamento e saida
    while cont <= casos:
        print(cont ** expo,cont ** (expo + 1), cont ** (expo + 2))
        print(cont ** expo, cont ** (expo + 1) + 1, cont ** (expo + 2) + 1)
        cont +=1

if __name__ == '__main__':
    main()