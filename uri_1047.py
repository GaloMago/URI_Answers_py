def main():

    # entrada
    hora_i,min_i,hora_f,min_f = map(int,input().split())

    # processamento
    if hora_i < hora_f:
        horas = hora_f - hora_i

    elif hora_i > hora_f:
        horas = (hora_f + 24) - hora_i

    elif hora_f == hora_i:
        horas = 24

        if min_i < min_f:
            horas = 0

    if min_i < min_f:
        minutos = min_f - min_i

    elif min_i > min_f:
        minutos = (min_f + 60) - min_i
        horas -= 1

    elif min_f == min_i:
        minutos = 0

    # saida
    print('O JOGO DUROU %d HORA(S) E %d MINUTO(S)'%(horas,minutos))

if __name__ == '__main__':
    main()

