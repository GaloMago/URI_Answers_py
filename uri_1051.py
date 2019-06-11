def main():
    #entrada
    salario = float(input())

    #processamento
    if 0 < salario <= 2000.00:
        print('Isento')

    elif 2000.01 <= salario <= 3000.00:
        cobrado = salario - 2000
        taxa = cobrado * (8/100)
        print('R$ %.2f' %taxa)

    elif 3000.01 <= salario <= 4500.00:
        cobrado = salario - 2000
        cobrado2 = cobrado - 1000
        taxa = 1000 * (8/100)
        taxa2 = cobrado2 * (18/100)
        print('R$ %.2f'%(taxa + taxa2))

    elif salario > 4500.00:
        cobrado = salario - 2000
        cobrado2 = cobrado - 1000
        taxa = 1000 * (8 / 100)
        cobrado3 = cobrado2 - 1500
        taxa2 = 1500 * (18/100)
        taxa3 = cobrado3 * (28/100)
        print('R$: %.2f' %(taxa+taxa2+taxa3))


if __name__ == '__main__':
    main()
