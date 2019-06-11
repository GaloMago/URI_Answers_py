def main():

    # dados
    i = 0
    j = 1
    j2 = 2
    j3 = 3
    cont = 0

    # processamento
    print('I=%d J=%d' % (i, j))
    print('I=%d J=%d' % (i, j2))
    print('I=%d J=%d' % (i, j3))
    i += 0.2
    j += 0.2
    j2 += 0.2
    j3 += 0.2

    # gambiarra e saida
    while i <= 2:
        if i == 1 or i >= 1.9 or j == 1 or j == 2 or j == 3:
            print('I=%.0f J=%.0f' % (i, j)) # %.0f arredonda o float pro inteiro mais próximo
            print('I=%.0f J=%.0f' % (i, j2))
            print('I=%.0f J=%.0f' % (i, j3))
        else:
            print('I=%.1f J=%.1f' %(i,j))
            print('I=%.1f J=%.1f' %(i,j2))
            print('I=%.1f J=%.1f' %(i,j3))

        i += 0.2
        j +=0.2
        j2 += 0.2
        j3 += 0.2

if __name__ == '__main__':
    main()