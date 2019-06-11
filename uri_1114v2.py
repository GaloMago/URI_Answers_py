def main():

    # dados
    senha = 2002

    while True:
        # entrada
        cod = int(input())

        # processamento
        if cod == senha:
            print('Acesso Permitido') # saida
            return False

        else:
            print('Senha Invalida') # saida

if __name__ == '__main__':
    main()