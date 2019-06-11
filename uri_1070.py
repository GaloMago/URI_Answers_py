def main():

    # entrada
    x = int(input())

    # processamento
    par6(x,6)

def par6(x,limite):
    while limite > 0:
        if x % 2 !=0:
            limite -= 1
            print(x)

        par6(x+1,limite)
        break

if __name__ == '__main__':
    main()