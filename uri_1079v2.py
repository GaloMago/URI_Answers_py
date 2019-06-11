def main():

    # entrada
    n = int(input())

    # processamento
    while n > 0:
        notas = input().split()
        nota1, nota2, nota3 = float(notas[0]),float(notas[1]),float(notas[2])
        media = ((nota1 * 2)+(nota2 * 3)+(nota3 * 5))/ 10
        print('%.1f'%media) # saida
        n -=1

if __name__ == '__main__':
    main()