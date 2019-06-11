def main():

    #entrada
    contador = 0
    for i in range (6):
        valor = float(input())

    #processamento e saida
        if valor > 0:
            contador += 1
    print("%d valores positivos" %contador)


if __name__ == '__main__':
    main()
