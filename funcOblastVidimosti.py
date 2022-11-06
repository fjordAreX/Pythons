a = 10

def name1():
    a = 9
    print(a)

name1()
print(a)

x = 5
def name2():
    global x # мы не создаем новую переменную, а берем ее извне метода
    x = 19
    print(x)

name2()
print(x)


def name3():
    global z
    z = 2
    print(z)

name3()
print(z)
print(2+z)
# мы создали переменную z благодаря global z в методе
# если метод не вызвать, то переменной не будет существовать

print('\n')

v = 1
def abob1():
    v = 2

    def abob2():
        v = 3
        print(v)

    abob2()
    print(v)

abob1()
print(str(v)+'\n\n')

# но если добавить во внутренний метод (abob2) слово nonlocal, то он будет работать с переменной
# которая была в методе выше (не глобальная переменная,а abob1)

c = 1
def aboba1():
    c = 2

    def aboba2():
        nonlocal c
        c = 3
        print(c)

    aboba2()
    print(c)

aboba1()
print(str(c)+'\n\n')


b = 1
def abobus1():
    b = 2

    def abobus2():
        global b
        b = 3
        print(b)

    abobus2()
    print(b)

abobus1()
print(b)