def main():

    # entrada
    entrega, data_f = map(int,input().split())

    # processamento e saidas
    if (data_f - entrega) >= 3 and data_f >= entrega:
        print('Muito bem! Apresenta antes do Natal!')
    elif (data_f - entrega) <=3 and data_f >= entrega:
        print('Parece o trabalho do meu filho!')
        entrega +=2

        if entrega < 24:
            print('TCC Apresentado!')
        else:
            print('Fail! Entao eh nataaaaal!')
    else:
        print('Eu odeio a professora!')

if __name__ == '__main__':
    main()