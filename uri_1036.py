def main():

    # entrada
    a,b,c = map(float,input().split())

    #processamento e saida
    delta = (b**2) - (4 * a * c)

    if delta == 0 or delta < 0 or a == 0:
        print('Impossivel calcular')

    else:
        r1 = (-b + (delta ** 0.5)) / (2*a)
        r2 = (-b - (delta ** 0.5)) / (2*a)
        print('R1 = %.5f\nR2 = %.5f'%(r1,r2))

if __name__ == '__main__':
    main()