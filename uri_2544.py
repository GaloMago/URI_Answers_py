def main():

    # entrada
    while True:
        try:
            naruto = int(input())
            cont = 0

            # processamento
            while naruto > 1:
                div = naruto // 2
                naruto = div
                cont +=1
            # saida
            print(cont)

        except EOFError:
            break

if __name__ == '__main__':
    main()