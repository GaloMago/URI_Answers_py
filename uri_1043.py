def main():

    # entrada
    a,b,c = map(float, input().split())

    #processamento e saida
    if (a + b) > c and (a + c) > b and (b + c) > a:
        perimetro = a + b + c
        print('Perimetro = %.1f'%perimetro)
    else:
        area = ((a + b) * c) / 2
        print('Area = %.1f'%area)

if __name__ == '__main__':
    main()