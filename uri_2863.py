def main():

    # entrada
    while True:
        try:
            corridas = int(input())
            menor = 11

            # processamento
            for i in range(corridas):
                tempo = float(input())
                if tempo <= menor:
                    menor = tempo
            # saida
            print(menor)
        except EOFError:
            break
if __name__ == '__main__':
    main()












if __name__ == '__main__':
    main()