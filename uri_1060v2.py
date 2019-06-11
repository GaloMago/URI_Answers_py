def main():

    # entrada
    n1 = float(input())
    n2 = float(input())
    n3 = float(input())
    n4 = float(input())
    n5 = float(input())
    n6 = float(input())
    contador = 0

    # processamento e saida
    if n1 > 0:
        contador +=1

    if n2 > 0:
        contador +=1

    if n3 > 0:
        contador +=1

    if n4 > 0:
        contador +=1

    if n5 > 0:
        contador +=1

    if n6 > 0:
        contador +=1

    print('%d valores positivos'%contador)

if __name__ == '__main__':
    main()