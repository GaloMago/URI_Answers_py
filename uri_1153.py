def main():

    # entrada
    n = int(input())
    fatorial = 1

    for i in range(n):
        fatorial = fatorial * (n-i)
    print(fatorial)


if __name__ == '__main__':
    main()