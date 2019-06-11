def main():
    #entrada
    senha = '2002'

    #processamento e saída
    while True:
        password = input()

        if password == senha:
            print("Acesso Permitido")
            break
        else:
            print("Senha Invalida")


if __name__ == '__main__':
    main()