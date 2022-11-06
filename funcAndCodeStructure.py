import math

PI = math.pi

def radius():
    n = float(input('Диаметр цилиндра в см: '))
    n /= 2
    return n

def height():
    m = float(input('Высота цилиндра в см: '))
    return m

def volume():
    r = radius()
    h = height()
    s = PI*r**2
    v = s*h
    return v

#print('Объем цилиндра',volume(),"см3")

def mass(g):
    n = float(input('Удельный вес цилиндра в г/см3: '))
    return g*n/1000

# аргумент функции - функция
if __name__ == '__main__':
    print('Вес цилиндра в кг: ',mass(volume()))