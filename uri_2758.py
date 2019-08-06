from decimal import Decimal
def main():

    # entrada
    a,b = map(float,input().split())
    c,d = map(float,input().split())

    # saida
    print('A = %.6ff, B = %.6ff'%(Decimal(a),Decimal(b)))
    print('C = {:f}, D = {:f}'.format(c,d))
    print('A = {:.1f}, B = {:.1f}'.format(a,b))
    print('C = {:.1f}, D = {:.1f}'.format(c,d))
    print('A = {:.2f}, B = {:.2f}'.format(a, b))
    print('C = {:.2f}, D = {:.2f}'.format(c, d))
    print('A = {:.3f}, B = {:.3f}'.format(a, b))
    print('C = {:.3f}, D = {:.3f}'.format(c, d))
    print('A = {:.3E}, B = {:.3E}'.format(a, b))
    print('C = {:.3E}, D = {:.3E}'.format(c, d))
    print('A = {:.0f}, B = {:.0f}'.format(a, b))
    print('C = {:.0f}, D = {:.0f}'.format(c, d))


if __name__ == '__main__':
    main(