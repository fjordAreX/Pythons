import os

h = [1,2,3,4,5,6,7,8,9]

# этот метод в два раза быстрее, чем классический метод создания пустого массива и заполнения через for

h1 = [x*2 for x in h] # список
print(h1)

h2 = {x*2 for x in h} # сет
print(h2)

h3 = {x : x*2 for x in h} # словарь (ключ - начальное число : значение - число после манипуляций, которые сам определяешь)
print(h3)

# генератор с условием
h4 = [x for x in h if x % 2 == 0]
print(h4)

h5 = [os.system('start' + os.path.join(address,file))
      for address,catalogs,files in os.walk('C:\\Users\\Генрик\\Desktop')
      for file in files
      if '.jpg' in file]

print(h5)

