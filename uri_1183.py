def main():

    # entrada
    matriz = criar_matriz(12,12)
    opera = input()
    preencher_matriz(matriz)
    print(acima_dig_principal_1183(opera,matriz))

# processamento e saida
def acima_dig_principal_1183(opera,matriz):
    soma = 0
    contador = 0
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if i < j:
                contador +=1
                soma += matriz[i][j]
    if opera == 'S':
        return soma
    else:
        return ('%.1f'%(soma/contador))

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