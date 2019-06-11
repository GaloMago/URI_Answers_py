def main():
    # entrada
    dias = int(input())

    # processamento
    ano = dias // 365
    meses = (dias % 365) // 30
    dias = (dias % 365) % 30

    # saida
    print('%d ano(s)\n%d mes(es)\n%d dia(s)'%(ano, meses, dias))

if __name__ == '__main__':
    main()