def main():
    #entrada
    X = 1
    spc =''

    #processamento
    while X != 0:
        X = int(input())
        for i in range (1, X+1):
            spc += str(i) + ' '
        print(spc[:-1])

if __name__ == '__main__':
    main()