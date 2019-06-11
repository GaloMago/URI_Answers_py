def main():
    #entrada
    notas = [float(x) for x in input().split()]

    #processamento e saída
    media = (notas[0] + notas[1] + notas[2] + notas[3]) / 4

    if media >= 7.0:
        print('Media: %.1f\nAluno aprovado.' %media)

    if media < 5.0:
        print('Media: %.1f\nAluno reprovado.' %media)

    elif  5.0 <= media <=6.9:
        print('Media: %.1f\nAluno em exame.'%media)
        examefinal = float(input())
        print('Nota do exame: %.1f'%examefinal)
        media2 = (media + examefinal) / 2

        if media2 >= 5.0:
            print('Aluno aprovado.\nMedia final: %.1f' %media2)

        else:
            print('Aluno reprovado.\nMedia final: %.1f' %media2)

if __name__ == '__main__':
    main()