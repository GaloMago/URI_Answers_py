def main():

    # entrada
    codigo, quantidade = map(int, input().split())
    #processamento
    if codigo == 1:
        preço = quantidade * 4.00
    elif codigo == 2:
        preço = quantidade * 4.50
    elif codigo == 3:
        preço = quantidade * 5
    elif codigo == 4:
        preço = quantidade * 2
    elif codigo == 5:
        preço = quantidade * 1.5

    print('Total : R$ %.2f'%(preço))

if __name__ == '__main__':
    main()