def main():

    while True:
        try:
            # entrada
            x_f,y_f,x_i,y_i,vel_i,r1,r2 = map(int,input().split())

            # processamento
            equação = ((x_f - x_i) ** 2 + (y_f - y_i) ** 2) ** (1/2) # equação da circunferência geral(distância entre os pontos)

            if r1 + r2 >= equação + 1.5 * vel_i: # se a soma dos raios for maior que a distância do alvo
                # saidas
                print('Y')
            else:
                print('N')

        except EOFError:
            break

if __name__ == '__main__':
    main()

# https://brasilescola.uol.com.br/matematica/equacao-reduzida-circunferencia.htm
