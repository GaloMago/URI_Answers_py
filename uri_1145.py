def main():
    #entrada
    n1, n2 = list(map(int, input().split()))
    cont = 1

    #processamento e saida
    for i in range(1, (int((n2 / n1)) + 1)):
        r = ""
        for y in range(n1):
            r += str(cont) + " "
            cont += 1
        print(r[:-1])

if __name__ == '__main__':
    main()