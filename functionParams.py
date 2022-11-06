def leng(x, count = 0):
    # в параметр можно вставлять переменную со значением(параметр по умолчанию)
    # параметр по умолчанию передается после аргумента (count = 0, x) - ошибка
    for _ in x:
    # если переменная не используется, ее можно заменить на черточку for i in x - for _ in x
        count += 1
    return count


j = [9,8,7,6,5]
print(leng(j))
h = ['a','a','h']
print(leng(h))
k = [4,5,1,3,8,1]
print(leng(k))

print(leng( (1,2,3,4,5) ))

print(leng([1,2,3]))
print()

# метод можно перегружать с помощью параметров по умолчанию (изменяя их)
def bob (x, boolean = False, count = 0):
    if boolean:
        for _ in x:
            count += 1
        return count-1, boolean
    else:
        for _ in x:
            count += 1
        return count

mh = [1,2,3,4,5,6]
print (bob(mh))
print (bob(mh,True))

var1,var2 = bob(mh,True)
print(var1)
print(var2)