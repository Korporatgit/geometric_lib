import math

def area(r):
    '''Принимает число r - радиус окружности, возвращает площадь круга 
       Параметры:
                r - длина радиуса окружности
        Возврващаемое значение:
                площадь круга
        Пример вызова:
            print(area(5))'''
    return math.pi * r * r


def perimeter(r):
    '''Принимает число r - радиус окружности, возвращает длину окружности
       Параметры:
                r - длина радиуса окружности
        Возврващаемое значение:
                длина окружности
        Пример вызова:
            print(perimetr(5))'''
    return 2 * math.pi * r

