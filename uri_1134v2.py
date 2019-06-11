def main():

    # entrada
    gas = 0
    alco = 0
    diesel = 0

    while True:
        combus = int(input())

        if combus == 1:
            alco +=1
        elif combus == 2:
            gas +=1
        elif combus == 3:
            diesel +=1

        elif combus == 4:
            print('MUITO OBRIGADO\nAlcool: %d\nGasolina: %d\nDiesel: %d'%(alco,gas,diesel))
            return False

if __name__ == '__main__':
    main()