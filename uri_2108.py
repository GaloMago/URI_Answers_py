def main():

    # dados base
    maior = 0
    maior_frase = ''


    while True:
        # entrada
        msg = input()
        # processamento//saida final
        if msg == '0':
            print('\nThe biggest word:',maior_frase)
            return False
        else:
            msg = msg.split()
            cont = 0
            for i in msg:
                # maior palavra de todas
                if len(i) >= maior:
                    maior = len(i)
                    maior_frase = i

                # saidas
                if cont == 0:
                    print('{}'.format(len(i)), end='')
                    cont +=1

                else:
                    print('-{}'.format(len(i)),end='')

if __name__ == '__main__':
    main()