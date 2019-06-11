def main():

    # dados
    pnt_gremio = 0
    pnt_inter = 0
    empate = 0
    grenal = 0

    while True:
        # entradas
        inter, gremio = map(int,input().split())

        # processamento
        if inter > gremio:
            pnt_inter +=1
        elif gremio > inter:
            pnt_gremio +=1
        else:
            empate +=1

        grenal +=1

        print('Novo grenal (1-sim 2-nao)')
        res = int(input())

        # mais processamento e saidas
        if res == 2:
            print('%d grenais\nInter:%d\nGremio:%d\nEmpates:%d'%(grenal,pnt_inter,pnt_gremio,empate))
            if pnt_inter > pnt_gremio:
                print('Inter venceu mais')
            elif pnt_inter < pnt_gremio:
                print('Gremio venceu mais')
            else:
                print('Nao houve vencedor')
            return False

if __name__ == '__main__':
    main()