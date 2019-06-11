def main():
    #entrada
    valores = input().split()
    A = float(valores[0])
    B = float(valores[1])
    C = float(valores[2])
    pi = 3.14159

    #processamento
    area_trg = (A*C)/2
    area_circ = pi * (C**2)
    area_trap = ((A + B) * C) / 2
    area_quad = B**2
    area_ret = A * B

    #saida
    print("TRIANGULO: %.3f" %area_trg)
    print("CIRCULO: %.3f" %area_circ)
    print("TRAPEZIO: %.3f" %area_trap)
    print("QUADRADO: %.3f" %area_quad)
    print("RETANGULO: %.3f" %area_ret)

if __name__ == '__main__':
    main()