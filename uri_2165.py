def main():

    # entrada
    tweet = input()
    # processamento e saida
    if len(tweet) <= 140:
        print('TWEET')
    else:
        print('MUTE')

if __name__ == '__main__':
    main()