def main():
    #entrada
    N = int(input())
    num = 1

    #processamento
    for i in range (N+1):
        if i > 0:
        #saida
            print("%d %d %d" %(i, i**2, i**3))
            num +=1


if __name__ == '__main__':
    main()