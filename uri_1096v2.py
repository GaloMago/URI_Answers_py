def main():

    # dados
    i = 1
    j = 7

    # processamento
    while j > 5 and i <= 9:
        print('I=%d J=%d'%(i, j)) # saida
        j -=1

        if j == 5:
            print('I=%d J=%d' %(i, j))  # saida
            i +=2
            j = 7

if __name__ == '__main__':
    main()
