def area(a, h): 
    '''Принимает числа a - сторона треугольника и h - высота в треугольнике, проведённая к этой стороне, возвращает площадь треугольника 
       Параметры:
                a - сторона треугольника
                h - высота в треугольнике, проведённая к этой стороне
        Возврващаемое значение:
                число - площадь треугольника
        Пример вызова:
            print(area(5, 10))'''
    return a * h / 2 

def perimeter(a, b, c): 
    '''Принимает числа a, b, c - стороны треугольника, возвращает периметр треугольника 
       Параметры:
                a - сторона треугольника
                b - сторона треугольника
                c - сторона треугольника 
        Возврващаемое значение:
                число - периметр треугольника
        Пример вызова:
            print(perimetr(3, 4, 5))'''
    return a + b + c 

