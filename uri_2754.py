def main():

    # dados
    x = 234.345
    y = 45.698

    # saida
    print('%.6f - %.6f'%(x,y))
    print('%.0f - %.0f'%(x,y))
    print('%.1f - %.1f'%(x,y))
    print('%.2f - %.2f'%(x,y))
    print('%.3f - %.3f'%(x,y))
    print('{:e} - {:e}'.format(x,y))
    print('{:E} - {:E}'.format(x,y))
    print('{} - {}'.format(x,y))
    print('{} - {}'.format(x,y))


if __name__ == '__main__':
    main()