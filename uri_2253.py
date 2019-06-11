def main():

    # entrada
    while True:
        try:
            senha = input()
            cont_M = 0 # maiusculas
            cont_m = 0 # minusculas
            cont_num = 0 # numeros
            cont_proi = 0 # proibidos

            # processamento
            for i in range(len(senha)):
                # caracteres proibidos
                if ord(senha[i]) in range(33,48) or ord(senha[i]) in range(58,65) or ord(senha[i]) in range(91,97) or ord(senha[i]) in range(123,256) or ord(senha[i]) == 32:
                    cont_proi +=1
                # maiúsculas,minúsculas e números requridos
                elif ord(senha[i]) in range(65,91):
                    cont_M +=1
                elif ord(senha[i]) in range(97,123):
                    cont_m +=1
                elif ord(senha[i]) in range(48,58):
                    cont_num +=1

            if cont_proi > 0 or len(senha) > 32 or len(senha) < 6:
                print('Senha invalida.')

            elif cont_M > 0 and cont_m > 0 and cont_num > 0:
                print('Senha valida.')
            else:
                print('Senha invalida.')

        except EOFError:
            break

if __name__ == '__main__':
    main()