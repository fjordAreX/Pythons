import funcAndCodeStructure
# импортируем что-то конкретное из модуля, в этом случае метод abob1
from funcOblastVidimosti import abob1

#импортируем всё из этого модуля, но в отличие от самого первого варианта импорта нам теперь не надо приписывать сначала модуль (тип не funcAndCodeStructure.PI, а просто PI)
from functionStart import *

import sys

# если название класса слишком длинное, то можно писать сокращение: (27 строка)
import funcVarietyOfArgs as fun

#смотрим какие там есть модули/методы/данные
print(dir(funcAndCodeStructure))

#info по разделам
print(help(funcAndCodeStructure))

print(funcAndCodeStructure.mass(2))
print(funcAndCodeStructure.PI)

abob1()
show()

print(sys.path)

print(fun.sortes([2,5,1,6,4,7,3]))

# if __name__ = '__main__'  сделано для того, чтобы добавляемые модули не запускались при добавлении (тип когда самостоятельная программа, тогда запускается)