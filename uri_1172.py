def main():

    # entrada
    vetor = [0] * 10

    # processamento
    for i in range(len(vetor)):
        vetor[i] = int(input())
        if vetor[i] <= 0:
            vetor[i] = 1
        # saida
        print('X[%d] = %d'%(i,vetor[i]))


if __name__ == '__main__':
    main()