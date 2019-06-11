def main():
    #entrada
    I = 1
    J = 7

    #processamento
    while I < 10:
        print('I=%d J=%d' %(I, J))

        if J == 5:
            I += 2
            J = 7
        else:
            J -=1

if __name__ == '__main__':
    main()