def main():
    # estilo do rogério
    # entrada
    resistente = input()
    amostra = input()
    codigo = ''
    cont = 0

    # saida
    if contem(amos,resistente) == True:
        print('Resistente')
    else:
        print('Não resistente')

# processamento
def verificar_string(t_amostra,inicio,fim):
    frase = ''
    while inicio <= fim:
        frase += t_amostra[inicio]
        inicio +=1
    return frase

def contem(amostra,resitente):
    t_amostra = len(amostra)
    t_res = len(resitente)
    inicio = 0

    while i <= (t_res - t_amostra):
        res = verificar_string(amostra,inicio, inicio + t_res - 1) # receberá a amostra e a cada loop avançará um caractere na string resistente
        if res == amostra:
            return True
        else:
            return False
        i +=1

if __name__ == '__main__':
    main()
