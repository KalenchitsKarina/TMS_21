'''
Дан список. Создать новый список, сдвинутый на 1 
элемент влево Пример:12345-> 23451
'''
ls=[23,12,4,5,0,'s',12]
print (ls)
f=ls[0]
for i in range (0,len(ls)-1):
    ls[i]=ls[i+1]
ls[len(ls)-1]=f
print (ls)

i=0
f=ls[0]
while i<len(ls)-1:
    ls[i]=ls[i+1]
    i+=1
ls[len(ls)-1]=f
print (ls)

