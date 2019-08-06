def main():

    while True:
        # entrada
        valores_area = list(map(int,input().split()))

        # processamento
        if valores_area[0] == 0:
            return False
        else:
            terreno = (valores_area[0] * valores_area[1] * 100 // valores_area[2]) ** (1/2)

            # saida
            print('%d'%terreno)

if __name__ == '__main__':
    main()