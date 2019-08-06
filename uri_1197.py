def main():

    while True:
        try:
            # entrada
            x,y = map(int,input().split())

            # processamento
            deslocamento = (x * y) * 2

            # saida
            print(deslocamento)

        except EOFError:
            break

if __name__ == '__main__':
    main()