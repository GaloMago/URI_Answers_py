def main():

    # entrada
    n1,n2,n3 = map(int, input().split())

    #processamento
    if n1 > n2 > n3:
        print(n3)
        print(n2)
        print(n1)

    elif n1 > n3 > n2:
        print(n2)
        print(n3)
        print(n1)

    elif n2 > n1 > n3:
        print(n3)
        print(n1)
        print(n2)

    elif n2 > n3 > n1:
        print(n1)
        print(n3)
        print(n2)

    elif n3 > n1 > n2:
        print(n2)
        print(n1)
        print(n3)

    elif n3 > n2 > n1:
        print(n1)
        print(n2)
        print(n3)

    print()
    print(n1)
    print(n2)
    print(n3)

if __name__ == '__main__':
    main()