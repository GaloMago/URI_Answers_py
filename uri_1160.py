def main():

    # entrada
    casos = int(input())
    pop_fa = 0 # população final A
    pop_fb = 0 # população final B

    # processamento
    for i in range(casos):
        anos = 0
        dados = input().split()
        pa,pb,g1,g2 = int(dados[0]),int(dados[1]),float(dados[2]),float(dados[3]) #população A, população B e crescimento
        while pa <= pb:
            pop_fa = pa + pa * ((g1/ 100))
            pop_fb = pb + pb * ((g2/100))
            pa = int(pop_fa)
            pb = int(pop_fb)
            anos +=1
            if anos > 100:
                break
        # saidas
        if anos > 100:
            print('Mais de 1 seculo.')
        else:
            print('%d anos.'%anos)

if __name__ == '__main__':
    main()