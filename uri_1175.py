def main():

    # entrada
    vetor = [0] * 20
    inverso = [0] * 20
    elementos = 19
    cont = 0

    # processamento
    for i in range(len(vetor)):
        vetor[i] = int(input())

    while elementos >= 0:
        inverso[cont] = vetor[elementos]
        # saida
        print('N[%d] = %d'%(cont,vetor[elementos]))
        elementos -=1
        cont +=1

if __name__ == '__main__':
    main()