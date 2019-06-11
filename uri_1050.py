def main():
    #entrada
    salario = float(input())

    #processamento e saida
    if  0 <= salario < 2000.01:
        print("Isento")

    elif 2000.01 <= salario <= 3000.00:
        sal_app = salario - 2000
        imposto = sal_app / 0.08
        print("R$ %.2f" %imposto)

    elif 3000.01 <= salario <= 4500.00:
        sal_app = salario - 2000
        sal_app2 = sal_app - 1000
        imposto1 = sal_app / 0.08
        imposto2 =  sal_app2 / 0.18
        total = imposto1 + imposto2
        print("R$ %.2f" %total)

    else:
        sal_app = salario - 2000
        sal_app2 = sal_app - 1000
        imposto1 = (1000 * 8) / 100
        sal_app3 = sal_app2 - 1500
        imposto2 = (1500 * 18) / 100
        imposto3 = (sal_app3 * 28) / 100
        total = imposto1 + imposto2 + imposto3
        print("R$ %.2f" %total)


if __name__ == '__main__':
    main()