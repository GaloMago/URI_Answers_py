def main():
    #entrada
    I = 0
    J = 1

    while I <= 2:
        for i in range (3):
            n = round(I, 1)
            if n % 1 == 0:
                if J % 1 == 0:
                    print('I={} J={}'.format(int(n), int(J+n)))
                else:
                    print('I={} J={}'.format(int(n), J + n))
            else:
                print('I={} J={}'.format(n, J + n))
            J +=1
        I += 0.2
        J = 1

if __name__ == '__main__':
    main()