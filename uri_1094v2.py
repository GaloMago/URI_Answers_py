def main():

    # entrada
    n = int(input())
    soma = 0
    coelhos = 0
    ratos = 0
    sapos = 0

    #processamento
    while n > 0:
        cobaia = input().split()
        num = int(cobaia[0])
        ser = cobaia[1]
        soma += num
        if ser == 'C':
            coelhos +=num
        if ser == 'R':
            ratos +=num
        if ser == 'S':
            sapos +=num
        n -=1
    per_coelho = (coelhos / soma) * 100
    per_ratos = (ratos / soma) * 100
    per_sapos = (sapos / soma) * 100

    # saida
    print('Total:',soma,'cobaias')
    print('Total de coelhos:',coelhos)
    print('Total de ratos:',ratos)
    print('Total de sapos:',sapos)
    print('Percentual de coelhos: %.2f %%\nPercentual de ratos: %.2f %%\nPercentual de sapos: %.2f %%'%(per_coelho,per_ratos,per_sapos))

if __name__ == '__main__':
    main()
