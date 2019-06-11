def main():

    # entrada
    dia_i = input().split()
    dia_i = int(dia_i[1])
    hora_inicial = input().split(':')
    dia_f = input().split()
    dia_f = int(dia_f[1])
    hora_final = input().split(':')
    hora_f, min_f, seg_f = int(hora_final[0]),int(hora_final[1]),int(hora_final[2])
    hora_i, min_i, seg_i = int(hora_inicial[0]),int(hora_inicial[1]),int(hora_inicial[2])

    #procesamento
    dias = dia_f - dia_i
    horas = hora_f - hora_i
    minutos = min_f - min_i
    segundos = seg_f - seg_i

    if horas < 0:
        horas +=24
        dias -=1

    if minutos < 0:
        minutos += 60
        horas -=1

    if segundos < 0:
        segundos +=60
        minutos -=1

    # saida
    print('%d dia(s)\n%d hora(s)\n%d minuto(s)\n%d segundo(s)'%(dias,horas,minutos,segundos))

if __name__ == '__main__':
    main()