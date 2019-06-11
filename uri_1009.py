def main():

    # entrada
    nome = input()
    SalFix = float(input())
    vendas = float(input())

    # processamento
    bonus = vendas * (15 / 100)
    total = SalFix + bonus

    # saida
    print('TOTAL = R$ %.2f' %total)

if __name__ == '__main__':
    main()