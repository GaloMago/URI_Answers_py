def main():

    # entrada
    a = float(input())
    b = float(input())
    c = float(input())
    d = float(input())
    e = float(input())
    contador_par = 0
    contador_pos = 0
    contador_neg = 0
    contador_imp = 0

    #processamento e saida
    if a % 2 == 0 and a > 0:
        contador_par +=1
        contador_pos +=1

    if a % 2 !=0 and a < 0:
        contador_neg +=1
        contador_imp +=1

    if a % 2 == 0 and a < 0:
        contador_par +=1
        contador_neg +=1

    if a % 2 !=0 and a > 0:
        contador_pos +=1
        contador_imp +=1

    #a
    if b % 2 == 0 and b > 0:
        contador_par += 1
        contador_pos += 1

    if b % 2 != 0 and b < 0:
        contador_neg += 1
        contador_imp += 1

    if b % 2 == 0 and b < 0:
        contador_par += 1
        contador_neg += 1

    if b % 2 != 0 and b > 0:
        contador_pos += 1
        contador_imp += 1
    #b
    if c % 2 == 0 and c > 0:
        contador_par += 1
        contador_pos += 1

    if c % 2 != 0 and c < 0:
        contador_neg += 1
        contador_imp += 1

    if c % 2 == 0 and c < 0:
        contador_par += 1
        contador_neg += 1

    if c % 2 != 0 and c > 0:
        contador_pos += 1
        contador_imp += 1
    #c
    if d % 2 == 0 and d > 0:
        contador_par += 1
        contador_pos += 1

    if d % 2 != 0 and d < 0:
        contador_neg += 1
        contador_imp += 1

    if d % 2 == 0 and d < 0:
        contador_par += 1
        contador_neg += 1

    if d % 2 != 0 and d > 0:
        contador_pos += 1
        contador_imp += 1

    if e % 2 == 0 and e > 0:
        contador_par += 1
        contador_pos += 1

    if e % 2 != 0 and e < 0:
        contador_neg += 1
        contador_imp += 1

    if e % 2 == 0 and e < 0:
        contador_par += 1
        contador_neg += 1

    if e % 2 != 0 and e > 0:
        contador_pos += 1
        contador_imp += 1

    if a == 0:
        contador_par +=1
    if b == 0:
        contador_par +=1
    if c == 0:
        contador_par +=1
    if d == 0:
        contador_par +=1
    if e == 0:
        contador_par +=1

    # saida
    print('%d valor(es) par(es)'%contador_par)
    print('%d valor(es) impar(es)'%contador_imp)
    print('%d valor(es) positivo(s)' %contador_pos)
    print('%d valor(es) negativo(s)' %contador_neg)

if __name__ == '__main__':
    main()