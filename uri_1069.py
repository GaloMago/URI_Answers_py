def main():

    # entrada
    casos = int(input())

    # processamento
    for i in range(casos):
        mineira = input()
        dia = 0
        mante = 0

        for j in range(len(mineira)):
            if mineira[j] == '<':
                dia +=1
            if mineira[j] == '>' and dia > 0:
                mante +=1
                dia -=1

        # saida
        print(mante)

if __name__ == '__main__':
    main()