#Задан целочисленный массив. Определить количество участков массива, на котором элементы монотонно возрастают (каждое следующее число больше предыдущего).

'''
from random import randint

while True:
    n=input('Enter size of array : ')
    if n.isdigit()==True:
        n=int(n)
        break
    else:
        print('n is not digit, try again!')
        continue
a=[randint(0,50) for i in range(n)]
print(a)

f=0
for i in range(n-1):
    if a[i]>a[i+1]:
        f+=1
print (f)
'''
index_s = 0
index_f = 0

ls = [3,4,5,6,7,4,4,3,5,6]
ls_m = []
for i in range(len(ls) - 1):
    if ls[i] < ls[i + 1]:
        if i == len(ls) - 1:
            index_f = i + 1
            ls_m.append([index_s, index_f]) 
    else:
        index_f = i
        ls_m.append([index_s, index_f])
        index_s = i + 1

print (ls_m)      