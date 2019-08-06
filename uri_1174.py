def main():

    # entrada
    vetor = [0] * 100

    # processamento
    for i in range(len(vetor)):
        valor = int(input())
        vetor[i] = valor
        if valor <= 10:
            print('A[%d] = %.1f' % (i, vetor[i]))

if __name__ == '__main__':
    main()