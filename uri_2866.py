def main():

    # entrada
    casos = int(input())

    # processamento
    for i in range(casos):
        sent = ''
        valor = input() # entradas

        for j in range(len(valor)):
            if 97 <= ord(valor[j]) <= 122:
                sent += valor[j]
        cont = len(sent) - 1
        cripto =''

        while cont >= 0:
            cripto +=sent[cont]
            cont -=1
        print(cripto) # saida

if __name__ == '__main__':
    main()