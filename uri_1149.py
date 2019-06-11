def main():
    #entrada
    lista = list(map(int, input().split()))

    n1 = 'I'
    n2 = 0
    soma = 0

    for i in lista:
        if (n1 == 'I'):
            n1 = i

        else:
            if (i > 0):
                n2 = i
                break

    for i in range(n2):
        soma += n1
        n1 += 1
    print("%d" % soma)


if __name__ == '__main__':
    main()


    def main():

        nest = []
        while True:
            t = list(input().split())
            nest += [t]
            print(nest)
            print(nested_sum(t))


    def nested_sum(nest):
        list = []
        soma = 0
        for i in range(len(nest)):
            nest[i] = int(nest[i])
            soma += nest[i]