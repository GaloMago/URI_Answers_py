def main():

    # entrada
    div = 1
    s = 0

    # processamento e saida
    while div <= 100:
        s += 1/div
        div +=1
    print('%.2f'%s)

if __name__ == '__main__':
    main()