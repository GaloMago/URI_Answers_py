def main():

    # entrada
    salario = float(input())

    #processamento e saida
    if 0 < salario <= 400:
        novo_salario = salario + (salario * 0.15)
        print('Novo salario: %.2f\nReajuste ganho: %.2f\nEm percentual: 15 %%'%(novo_salario,(salario * 0.15)))

    elif 400 < salario <= 800:
        novo_salario = salario + (salario * 0.12)
        print('Novo salario: %.2f\nReajuste ganho: %.2f\nEm percentual: 12 %%' %(novo_salario, (salario * 0.12)))

    elif 800 < salario <= 1200:
        novo_salario = salario + (salario * 0.1)
        print('Novo salario: %.2f\nReajuste ganho: %.2f\nEm percentual: 10 %%' % (novo_salario, (salario * 0.1)))

    elif 1200 < salario <= 2000:
        novo_salario = salario + (salario * 0.07)
        print('Novo salario: %.2f\nReajuste ganho: %.2f\nEm percentual: 7 %%' % (novo_salario, (salario * 0.07)))

    else:
        novo_salario = salario + (salario * 0.04)
        print('Novo salario: %.2f\nReajuste ganho: %.2f\nEm percentual: 4 %%' % (novo_salario, (salario * 0.04)))

if __name__ == '__main__':
    main()
