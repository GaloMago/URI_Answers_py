def main():

    # entrada
    casos = int(input())

    # processamento
    for i in range(casos):
        led = 0
        lamp = input()
        for j in range(len(lamp)):
            if lamp[j] == '1':
                led += 2
            elif lamp[j] == '2' or lamp[j] == '3' or lamp[j] == '5':
                led += 5
            elif lamp[j] == '4':
                led += 4
            elif lamp[j] == '6' or lamp[j] == '9' or lamp[j] == '0':
                led += 6
            elif lamp[j] == '7':
                led += 3
            elif lamp[j] == '8':
                led += 7

        # saida
        print(led,'leds')

if __name__ == '__main__':
    main()