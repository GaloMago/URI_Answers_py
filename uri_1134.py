def main():
    #entrada
    cont_gas = 0
    cont_alc = 0
    cont_diel = 0
    N = 0

    #processamento
    while N != 4:
        N = int(input())
        if N == 1:
            cont_alc +=1
        elif N == 2:
            cont_gas +=1
        elif N == 3:
            cont_diel +=1
        elif N == 4:

            #saida
            print("MUITO OBRIGADO")
            print("Alcool: %d" %cont_alc)
            print("Gasolina: %d" %cont_gas)
            print("Diesel: %d" %cont_diel)





if __name__ == '__main__':
    main()