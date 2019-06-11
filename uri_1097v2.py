def main():

    # dados
    i = 1
    j = 7

    # processamento
    while j > (j - 2) and i <= 9:
        print('I=%d J=%d' % (i, j))  # saida
        j -=1

        if j == 5 or j == 7 or j == 9 or j == 11 or j == 13:
            print('I=%d J=%d' % (i, j)) # saida
            j += 4
            i += 2

if __name__ == '__main__':
    main()