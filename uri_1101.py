def main():

    while True:
        soma = 0
        texto = ''
        M, N = [int(i) for i in input().split()]
        if M <= 0 or N <= 0:
            break
        elif M <= N:
            for i in range(M, N + 1):
                soma += i
                texto += str(i) + ' '
        elif M > N:
            for i in range(N, M + 1):
                soma += i
                texto += str(i) + ' '
        print(texto + ('Sum=%d' % soma))

if __name__ == '__main__':
    main()