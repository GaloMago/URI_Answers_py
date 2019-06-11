def main():

    # entrada
    x = int(input())
    contador = 0

    # processamento e saida
    while contador < x:
        contador +=1
        if contador % 2 != 0:
            print(contador)

if __name__ == '__main__':
    main()