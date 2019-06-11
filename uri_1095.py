def main():
    #entrada
    I = 1
    J = 60

    #processamento e saida
    print('I=%d  J=%d' % (I, J))
    while J > 0:
        I +=3
        J -=5
        print('I=%d  J=%d' %(I, J))

if __name__ == '__main__':
    main()