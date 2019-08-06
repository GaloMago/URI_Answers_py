def main():

    # entrada
    temp_a,temp_b,temp_c = map(int,input().split())

    # processamento
    dife = temp_b - temp_a
    dif2 = temp_c - temp_b

    # saida
    if temp_b < temp_a and temp_c >= temp_b or temp_b > temp_a and temp_c > temp_b and dife <= dif2 or temp_a > temp_b and temp_b > temp_c and temp_b - temp_c < temp_a - temp_b or temp_a == temp_b and temp_c > temp_b:
        print(':)')
    else:
        print(':(')

if __name__ == '__main__':
    main()