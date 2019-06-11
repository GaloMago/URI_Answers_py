def main():
    #entrada
    #cartas = list(map(int,input().split()))
    #contador_rep = 0

    #processamento e saida
    #for i in range(len(cartas)):
        #if cartas[i] > 13 or cartas[i] <= 0:
            #contador_rep +=1
            #if contador_rep == 1:
                #return main()

    #if (len(cartas)) == 5:
        #if cartas == sorted(cartas):
            #print("C")

    #if cartas == sorted(cartas, key=int, reverse = True):
          #print("D")

    #elif cartas != sorted(cartas) and cartas != sorted(cartas, key=int, reverse = True):
        #print("N")

    #solução
    cartas = [int(x) for x in input().split()]

    if cartas == sorted(cartas):
        print('C')
    elif cartas == sorted(cartas, reverse=True):
        print('D')
    else:
        print('N')
if __name__ == '__main__':
    main()