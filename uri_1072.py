def main():

    # entrada
    n = int(input())
    cont_in = 0
    cont_out = 0

    # processamento
    while n > 0:
        valor = int(input())
        if 10 <= valor <= 20:
            cont_in +=1
        else:
            cont_out +=1
        n -=1
    # saida
    print('%d in\n%d out'%(cont_in,cont_out))

if __name__ == '__main__':
    main()