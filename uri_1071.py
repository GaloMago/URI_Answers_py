def main()

    # entrada
    x = int(input())
    y = int(input())

    # processamento
    impares_bet(x,y)

def impares_bet(x,y):
    impar = 0
    soma = 0
    if x > y:
        while x > y:
            if x % 2 !=0:
                impar += x

            print(impar)
        impares_bet(x-1,y)

    elif y > x:
        while y > x:
            if y % 2 !=0:
                impar += y

            print(impar)

        impares_bet(x,y-1)
