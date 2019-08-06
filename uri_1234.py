def main():

    # entrada
    while True:
        try:
            sent = input()
            dance = ''
            contador = 0

            # processamento
            for letra in range(len(sent)):
                if ord(sent[letra]) in range (97,123):
                    if contador % 2 == 0:
                        dance += chr(ord(sent[letra]) - 32)
                    else:
                        dance += sent[letra]
                    contador +=1
                elif ord(sent[letra]) in range(65,91):
                    if contador % 2 != 0:
                        dance += chr(ord(sent[letra])+32)
                    else:
                        dance +=sent[letra]
                    contador +=1
                else:
                    dance += sent[letra]
            # saida
            print(dance)

        except EOFError:
            break
if __name__ == '__main__':
    main()