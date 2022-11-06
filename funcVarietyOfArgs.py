def name (*args):
    print(args)

name()
name(1)
name(1,2,3,4,5)

def namor (h, *args):
    print(h)
    print(args)

namor(1)
namor(1,2,3,4,5)
# namor() - выдает ошибку, тк требуется аргумент h обязательно, а *args необязателен

def namore (h = 1, *args):
    print(h)
    print(args)

namore()
namore(1,2,3) # первый аргумент все равно идет к параметру h

# мы можем поставить после *args еще один параметр,
# но чтобы он заработал нужно в аргументе к нему напрямую обратиться

def namorel(h = 1, * args, key):
    print(h, end=' ')
    print(args,end=' ')
    print(key)

namorel(1,2,3,4,5,key = 6)

print(1,2,3,4,5, sep='!')

def sortes(x):
    for i in range(len(x)):
        for j in range(i+1,len(x)):
            if x[j] < x[i]:
                x[j],x[i] = x[i],x[j]
    return x

print(sortes([4,2,3,5,1]))


def Henryk(love):
    if love == 'Kamilla':
        return True
    else:
        return 'no, i want my wife'

print(Henryk('Kamilla'))
print(Henryk('Biba'))