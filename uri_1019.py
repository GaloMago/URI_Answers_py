def main():
    # entrada
    N = int(input())

    # processamento
    conv_horas = N // 3600
    conv_minutos = (N // 60) % 60
    segundos = (N % 3600) % 60

    # saida
    print('%d:%d:%d' %(conv_horas, conv_minutos, segundos))

if __name__ == '__main__':
    main()