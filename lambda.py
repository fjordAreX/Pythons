from dis import dis

def some(x):
    return x/5

var = lambda x: x / 5

print(some(10))
print(var(10))

print(dis(some))
print(dis(var))

# def some == lambda ;  (x): == x:  ;  return x/5 == x/5

# удобно использовать для: сортировки, фильтрации


list_of = [['Adam',29],['Johny',3*1/12],['Jess',25]]

def s(x):
    return x[1]
r = sorted(list_of, key = s) # key = ключ сортировки, метод которым сортируется
print(r)

r1 = sorted(list_of, key = lambda x:x[1])
print(r1)

x = list(filter(lambda z: z[1]>18, list_of)) # stream().filter(z->z>18)
print(x)