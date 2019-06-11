def main():

    # entrada
    while True:
        a, b = map(int,input().split())
        if cres_des(a,b) == False:
            return False

        # saida
        print(cres_des(a,b))

def cres_des(a,b):
    if a > b:
        return 'Decrescente'
    elif b > a:
        return 'Crescente'
    else:
        return False

if __name__ == '__main__':
    main()