def main():

    # entrada
    vert_invert = input()

    # processamento e saida
    if vert_invert == 'vertebrado':
        ave_mami = input()

        if ave_mami == 'ave':
            carni_oni = input()

            if carni_oni == 'carnivoro':
                print('aguia')

            elif carni_oni == 'onivoro':
                print('pomba')

        elif ave_mami == 'mamifero':
            carni_oni = input()

            if carni_oni == 'onivoro':
                print('homem')

            elif carni_oni == 'herbivoro':
                print('vaca')

    elif vert_invert == 'invertebrado':
        anel_inseto = input()

        if anel_inseto == 'inseto':
            hema_herbi = input()

            if hema_herbi == 'hematofago':
                print('pulga')

            elif hema_herbi == 'herbivoro':
                print('lagarta')

        elif anel_inseto == 'anelideo':
            hema_oni = input()

            if hema_oni == 'hematofago':
                print('sanguessuga')

            elif hema_oni == 'onivoro':
                print('minhoca')

if __name__ == '__main__':
    main()