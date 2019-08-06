def main():

    while True:
        try:
            # entrada
            perna = input()

            # saidas
            if perna == 'esquerda':
                print('ingles')
            elif perna == 'direita':
                print('frances')
            elif perna == 'nenhuma':
                print('portugues')
            elif perna == 'as duas':
                print('caiu')
        except EOFError:
            break

if __name__ == '__main__':
    main()