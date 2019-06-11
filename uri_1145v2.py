def main():

    # entrada
    x, y = map(int,input().split())

    # processamento e saida
    for i in range(1,y+1):
        if i % x == 0:
            print(i,end='\n')
        else:
            print(i,end=' ')

if __name__ == '__main__':
    main()
