def main():

    # criação de matriz
    matriz = criar_matriz(12,12)

    # entradas
    opera = input()
    preencher_matriz(matriz)

    # processamento
    if opera == 'S':
        soma = 0
        for i in range(len(matriz)):
            for j in range(len(matriz[i])):
                if j + i > len(matriz) - 1 and j < i and i > 6: # a soma da linha + coluna é maior que o número de casas,essa é a condição para a diagonal secundária. Para a principal é necessário que a numero da linha seja menor que a da coluna e maior que 6.
                    soma += matriz[i][j]
        # saida
        print('%.1f'%soma)

    else:
        soma = 0
        contador = 0
        for i in range(len(matriz)):
            for j in range(len(matriz[i])):
                if j + i > len(matriz) - 1 and j < i and i > 6:
                    soma += matriz[i][j]
                    contador +=1
        # saida
        print('%.1f' %(soma/contador))

# funções
def criar_matriz(li, co):
    vetor = [0] * li

    for i in range(len(vetor)):
        vetor[i] = [0] * co

    return vetor

def preencher_matriz(matriz):
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            matriz[i][j] = float(input())

if __name__ == '__main__':
    main()