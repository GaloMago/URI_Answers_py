def main():
    #entrada
    N = int(input())

    #processamento e saida
    for i in range (1, 11):
        mult = N * i
        print('%d x %d = %d' %(i, N, mult))

if __name__ == '__main__':
    main()

