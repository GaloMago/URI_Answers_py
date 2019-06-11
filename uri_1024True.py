def main():

    N = int(input())
    contador = 0

    while contador < N:
        frase = input()
        criptografia1024(frase)
        contador +=1

def criptografia1024(frase):
    pos = 0
    nova_frase = ''

    while pos < len(frase):
        ascii = ord(frase[pos]) #pos. ascii
        if 65 <= ascii <= 90 or 97 <= ascii <= 122: #letras maiusculas e minusculas
            movimento = ascii + 3 # deslocamento
            nova_frase += chr(movimento) #primeira leitura
        else:
            nova_frase += frase[pos]

        pos +=1 # termino das condições da 1º leitura
    nova_frase = nova_frase[::-1] # inversão // segunda leitura

    #terceira etapa: divisão pela metade
    div = (len(nova_frase) / 2) # metade do tamanho da string
    cont = 0
    codigo = ''

    while cont < len(nova_frase):
        if div % 2 != 0:
            if cont <= div - 1:
                codigo += nova_frase[cont]
            else:
                desloc = ord(nova_frase[cont]) - 1
                codigo += chr(desloc)

        else:
            if cont <= div - 1 :
                codigo +=nova_frase[cont]
            else:
                desloc = ord(nova_frase[cont]) - 1
                codigo += chr(desloc)

        cont +=1
    print(codigo)

if __name__ == '__main__':
    main()