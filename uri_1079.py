def main():
    #entrada
    N = int(input())

    #processamento e saida
    for i in range (N):
        Valores = list(map(float, input().split()))
        v1, v2, v3 = Valores
        v1 = v1 * 2
        v2 = v2 * 3
        v3 = v3 * 5
        media = (v1 + v2 + v3)/10
        print('%.1f' %media)
if __name__ == '__main__':
    main()

