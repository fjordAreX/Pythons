import os
import time

# проходит по операционной системе и ищет в ней
# он входит по указанному адресу и ходит по всем файлам и папкам внутри
for i in os.walk('C:\\Users\Генрик\Desktop\example'):
    print(i)
    break
# выдает кортеж с тремя элементами внутри картежа : 1) указанный путь, 2) папки по пути 3)файлы по пути

for i in os.walk('C:\\Users\Генрик\Desktop\example'):
    print(i)

print()

lista = []

# поскольку это картеж мы можем брать его элементы в переменные
for address, directories, files in os.walk('C:\\Users\Генрик\Desktop\example'):
    print('address is',address)
    print('directories are', directories)
    print('files are', files)

    # выведем полный адрес для каждого файла
    for file in files:
        x = os.path.join(address,file) # соединяет по правилам операционной системы на которой работает
        if '.jpg' in x:
            lista.append(x)

for i in lista:
    os.system('start '+i)
    print(i)
    print(os.path.getctime(i)) # выводит время создания файла в секундах c начала эпохи(какой эпохи?)
    # для вывода времени (в секундах) с момента создания файла:
    print(time.time() - os.path.getctime(i))