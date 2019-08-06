def main():

    # entrada
    while True:
        try:
            # entrada
            texto = input()
            cont_i = 0
            cont_b = 0
            nova_frase = ''
            # processamento
            for i in range(len(texto)):
                if texto[i] == '_':
                    cont_i +=1
                    if cont_i % 2 != 0:
                        nova_frase +='<i>'
                    else:
                        nova_frase +='</i>'
                elif texto[i] == '*':
                    cont_b +=1
                    if cont_b % 2 !=0:
                        nova_frase +='<b>'
                    else:
                        nova_frase +='</b>'
                else:
                    nova_frase += texto[i]

            # saida
            print(nova_frase)

        except EOFError:
            break

if __name__ == '__main__':
    main()