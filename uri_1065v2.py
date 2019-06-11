def main():

    # entrada
    n1 = float(input())
    n2 = float(input())
    n3 = float(input())
    n4 = float(input())
    n5 = float(input())
    contador = 0

    # processamento
    if n1 % 2 == 0:
        contador +=1

    if n2 % 2 == 0:
        contador +=1

    if n3 % 2 == 0:
        contador +=1

    if n4 % 2 == 0:
        contador +=1

    if n5 % 2 == 0:
        contador +=1

    print('%d valores pares'%contador)

if __name__ == '__main__':
    main()