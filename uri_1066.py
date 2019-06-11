def main():
    #entrada
    cont_par = 0
    cont_imp = 0
    cont_neg = 0
    cont_pos = 0

    #processamento
    for i in range (5):
        valor = int(input())
        if valor % 2 == 0:
            cont_par +=1

        if valor % 2 != 0:
            cont_imp += 1

        if valor > 0:
            cont_pos +=1

        if valor < 0:
            cont_neg +=1

    #saida
    print("%d valor(es) par(es)" %cont_par)
    print("%d valor(es) impar(es)" % cont_imp)
    print("%d valor(es) positivo(s)" %cont_pos)
    print("%d valor(es) negativo(s)" %cont_neg)


if __name__ == '__main__':
    main()