import os

list_paths = []

for address,directs,files in os.walk('C:\\Users\Генрик\Desktop'):
    for file in files:
        if '.txt' in file and 'lol' in address:
            full_path = os.path.join(address,file)
            list_paths.append(full_path)


# regimes:
# r - чтение(стоит по умолчанию)
# t - текстовый режим
# w - запись (все до этого удаляется, если файла нет, то создается)
# a - дозапись (в конец файла добавляется, если файла нет, то создается)
# b - бинарный режим (работа с exe и тд)
# + - открыть для чтения и записи (r+,w+,a+) (?)

# open(file,regime,encoding=) file - пишем полный путь, если нужный файл не в одной папке со скриптом
for i in list_paths:
    r = open(i,'w')
    r.write('One Line of text')
    r.close()

for i in list_paths:
    r = open(i)
    u = r.read()
    print(u)
    r.close()


# делаем копию exe файла:

r = open('C:\\Program Files (x86)\PrivaZer\PrivaZer.exe','rb')
y = open('C:\\Users\Генрик\Desktop\CopyZ.exe','wb')
# r считывает файл из папки, y записывает на рабочий стол

while True: # записывать будем по частям, чтобы не перегрузить оперативку
    var = r.read(1048576) # в скобках можно указать объем чтения в байтах - у нас 1 мб
    print(var.__sizeof__())
    y.write(var)
    if var.__sizeof__() == 33:
        break

print('Done')
r.close()
y.close()
