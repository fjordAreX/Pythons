import os

for address, catalogs, files in os.walk('C:\\Users\Генрик\Desktop\example-lol'):
    for file in files:
        if '.jpg' in file:
            x = os.path.join(address,file)
            os.system('start '+ x)