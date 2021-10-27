#В массиве целых чисел с количеством элементов 19 определить максимальное число и заменить им все четные по значению элементы.

from array import *
from random import randint

a=[randint(0,50) for i in range(19)]
print(a)

f=0                            
for i in range (19):          #нашли самый большой элемент f
    if a[i]>f:
        f=a[i]
print(f)
for i in range (19):          #заменили все четные на f
    if a[i]%2==0:
        a[i]=f
print(a)
