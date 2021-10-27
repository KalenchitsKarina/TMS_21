'''
Дан список целых чисел. 
Подсчитать сколько четных чисел в списке
'''

ls=[22,1,0,-3,55,12,78]
f=0
for i in range(0,len(ls)):
    if ls[i]%2==0:
        f+=1
print ('There are ',f,'even numbers in the list')

i=0
f=0
while i<len(ls):
    if ls[i]%2==0:
        f+=1
    i+=1
print ('There are ',f,'even numbers in the list')