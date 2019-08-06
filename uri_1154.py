def main():

    cont = 0
    soma = 0

    while True:
        # entrada
        idade = int(input())
        # processamento
        if idade >= 0:
            cont +=1
            soma += idade

        # saida
        if idade < 0:
            media = soma / cont
            print('%.2f'%media)
            return False

if __name__ == '__main__':
    main()