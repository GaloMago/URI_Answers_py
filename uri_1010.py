def main():
    #entrada
    valores = input().split()
    valores_2 = input().split()

    #processamento
    cdg = int(valores[0])
    qtd = int(valores[1])
    valor = float(valores[2])

    cdg2 = int(valores_2[0])
    qtd2 = int(valores_2[1])
    valor2 = float(valores_2[2])

    total = (qtd * valor) + (qtd2 * valor2)
    #saida

    print("VALOR A PAGAR: R$ %.2f" %total)


if __name__ == '__main__':
    main()