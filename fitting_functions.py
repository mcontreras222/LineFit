def linear(m, x, b):
    return m*x+b

def slope_units(x_units, y_units):
    xu = x_units.rstrip('s')
    yu = y_units.rstrip('s')
    return yu+'/'+xu


def print_equation(m, b, x_units, y_units):
    s_units = slope_units(x_units, y_units)

    print('The equation of the line is: y =', end=' ')

    if m != 0:
        print(m,s_units,'x', end=' ')
        if b>0:
            print('+', b, y_units.rstrip('s'))
        elif b<0:
            print('-', abs(b), y_units.rstrip('s'))
    else:
        if b != 0:
            print(b, y_units.rstrip('s'))
        else:
            print(0)
