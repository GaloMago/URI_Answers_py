def main():

    # entrada
    while True:
        string = input()
        if string == ValueError:
            print('error')
        else:
            numeral = ''

            for i in range(len(string)):
                if string[i] == 'O' or string[i] == 'o':
                    numeral +='0'
                elif string[i] == 'l':
                    numeral += '1'
                elif string[i] == ',' or string[i] == ' ':
                    numeral +=''

if __name__ == '__main__':
    main()