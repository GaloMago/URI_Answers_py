def main():
    #entrada
    I = 1
    J = 7

    #processamento e saída
    while I < 10:
        for i in range(3):
            print("I=%d J=%d" %(I, J))
            J += -1

        I += 2

        J = I + 6

if __name__ == '__main__':
    main()