def main():
    #entrada
    tempo = int(input())
    velocidade = int(input())

    #processamento
    litros = (tempo * velocidade) / 12

    #saida
    print("%.3f" %litros)

if __name__ == '__main__':
    main()