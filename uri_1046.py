def main():

    # entrada
    hora_inicial,hora_final = map(int,input().split())

    # processamento
    if hora_inicial > hora_final:
        hora_final += 24
        total = hora_final - hora_inicial

    elif hora_inicial < hora_final:
        total = hora_final - hora_inicial

    elif hora_final == hora_inicial:
        total = 24

    # saida
    print('O JOGO DUROU %d HORA(S)'%total)

if __name__ == '__main__':
    main()