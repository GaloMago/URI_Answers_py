def main():

    #entrada
    cord_p1 = input().split()
    x1 = float(cord_p1[0])
    y1 = float(cord_p1[1])

    cord_p2 = input().split()
    x2 = float(cord_p2[0])
    y2 = float(cord_p2[1])

    #processamento
    distancia = ((x2 - x1)**2 + (y2 - y1)**2)**0.5

    #saida
    print("%.4f" %distancia)


if __name__ == '__main__':
    main()