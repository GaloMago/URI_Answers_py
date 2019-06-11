def main():
    #entrada
    N = int(input())
    Num = 1

    for i in range (1, N):
        print("%d %d %d PUM" %(Num, Num+1, Num+2))
        Num +=4

if __name__ == '__main__':
    main()