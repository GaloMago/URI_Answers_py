def main():

    # entrada
    n = int(input())
    cont = 1

    # processamento e saida
    while cont < 10000:
        if cont % n == 2:
            print(cont)
        cont +=1

if __name__ == '__main__':
    main()