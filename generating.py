# generator function, оператор yield создает из функции объект-генератор
# обычный способ предполагает что мы в переменную в цикле получаем через return list весь список из слов, все объекты,
# а оператор yield предполагает, что мы в переменную в цикле получаем по одному элементу за одну итерацию
# (то есть память не так нагружена, ибо мы весь список разом не выгружаем и не ходим по нему, а просто получаем по одному элементу)
# в примере с some() и gen_some() мы получаем, что из some() мы берем весь лист со всеми строками и ходим по нему,
# а из some() мы за итерацию вытаскиваем из метода одну строку кода, что разгружает память,
# Например в ситуации когда нам нужно взять только некоторые строки - тогда мы не будем загружать в память лишние строки

def some():
    list_text = []
    with open('text.txt',encoding='utf-8') as r:
        for x in r:
            list_text.append(x)
    return list_text

print(some())

for i in some():
    print(i)

for i in some():
    print(i.split())

print ('\nNow witch generator\n')

def gen_some():
    with open('text.txt', encoding='utf-8') as r:
        for x in r:
            yield x


print((gen_some()))

for i in gen_some():
    print(i)

for i in gen_some():
    print(i.split())