def main():

    while True:
        try:
            # entrada
            cod = input()
            res = input()

            # processamento e saida
            if res in cod:
                print('Resistente')
            else:
                print('Nao resistente')
        except EOFError:
            break

if __name__ == '__main__':
    main()