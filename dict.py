# dict = HashMap

# создание
d1 = {'a':7}
d2 = dict(a=7)
d3 = dict.fromkeys([1,2,3], 'value') # каждый элемент списка слева имеет значения справа
print(d1['a'])
d1['b'] = 9
print(d1['b'])
print(d1)
d1['a'] = 8
print(d1)
del d1['a']
print(d1)
print(d2)
print(d3)

users = {'a':{'pass':123},'b':{'pass':435}}
print(users.items())

for a,b in users.items():
    print(a)
    for c,d in b.items():
        print(c)
        print(d)

d4 = dict([['key1','value2'],['key2','value2'],['key3','value3']])
print(d4)

d1 = {1:2,2:3,1:3}
print(d1)