def main():
    #entrada
    valor = float(input())

    #processamento
    nota_100 = valor / 100
    resto = valor % 100
    nota_50 = resto / 50
    resto = resto % 50
    nota_20 = resto / 20
    resto = resto % 20
    nota_10 = resto / 10
    resto = resto % 10
    nota_5 = resto / 5
    resto = resto % 5
    nota_2 = resto / 2
    resto = resto % 2
    nota_1 = resto / 1
    resto = resto % 1

    moeda_50 = resto / 0.5
    resto = resto % 0.5
    moeda_25 = resto / 0.25
    resto = resto % 0.25
    moeda_10 = resto / 0.10
    resto = resto % 0.10
    moeda_5 = resto / 0.05
    resto = resto % 0.05
    moeda_1 = resto / 0.01 + 0.001


    #saída
    print("NOTAS:")
    print("%d nota(s) de R$ 100.00" %nota_100)
    print("%d nota(s) de R$ 50.00" %nota_50)
    print("%d nota(s) de R$ 20.00" %nota_20)
    print("%d nota(s) de R$ 10.00" %nota_10)
    print("%d nota(s) de R$ 5.00" %nota_5)
    print("%d nota(s) de R$ 2.00" %nota_2)
    print("MOEDAS:")
    print("%d moeda(s) de R$ 1.00" % nota_1)
    print("%d moeda(s) de R$ 0.50" % moeda_50)
    print("%d moeda(s) de R$ 0.25" % moeda_25)
    print("%d moeda(s) de R$ 0.10" % moeda_10)
    print("%d moeda(s) de R$ 0.05" % moeda_5)
    print("%d moeda(s) de R$ 0.01" % moeda_1)

if __name__ == '__main__':
    main()