def main():

    # entrada
    n1,n2,n3,n4 = map(float, input().split())

    #processamento e saida
    media = (n1*2 + n2*3 + n3*4 + n4) / 10
    print('Media: %.1f'%(media))

    if media >= 7:
        print('Aluno aprovado.')

    elif media < 5:
        print('Aluno reprovado.')

    elif 5 <= media <= 6.9:
        print('Aluno em exame.')
        exame = float(input())

        print('Nota do exame: %.1f'%exame)
        nova_media = (media + exame) / 2

        if nova_media >= 5:
            print('Aluno aprovado.\nMedia final: %.1f'%(nova_media))

        else:
            print('Aluno reprovado\nMedia final: %.1f'%(nova_media))

if __name__ == '__main__':
    main()