def main():

    # processamento
    contador = 1
    maior = 0
    pos = 0

    while contador <= 100:
        valor = int(input())
        if valor > maior:
            maior = valor
            pos = contador
        contador +=1

    # saida
    print(maior)
    print(pos)
if __name__ == '__main__':
    main()