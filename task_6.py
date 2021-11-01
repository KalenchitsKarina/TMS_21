from random import randint

a=int(input('Enter the lower limit of the matrix range : '))
b=int(input('Enter the upper limit of the matrix range : '))
n=int(input('Enter n (size of matrix) : '))
m=int(input('Enter m (size of matrix) : '))

matrix = []

for i in range (n):
    matrix.append([])

for i in range(n):
    for j in range (m):
        matrix[i].append(randint(a,b))

print ()
print ('matrix :')
for i in matrix:
    print (i)

max=matrix[0][0]
min=matrix[0][0]
summ=0
maxrow=sum(matrix[0])
imaxrow=0
minrow=sum(matrix[0])
iminrow=0
f=0

for i in range (n):
    f=0
    for j in range (m):         #проход по элементам
        if matrix[i][j]>max:    #поиск наибольшего
            max=matrix[i][j]     
        if matrix[i][j]<min:    #поиск наименьшего
            min=matrix[i][j]
        summ+=matrix[i][j]      #cумма всех элементов
        f+=matrix[i][j]         #cумма элементов ряда
    if maxrow<f:                #поиск ряда с максимальной суммой эл
        maxrow=f
        imaxrow=i
    if minrow>f:                #поиск ряда с минимальной суммой эл
        minrow=f
        iminrow=i
print ('maximum matrix element : ',max )
print ('minimum matrix element : ', min)
print ('summ of elements : ',summ)
print ('index of the row with the maximum sum of elements : ', imaxrow)
print ('index of the row with the minimum sum of elements : ', iminrow)

maxcolumn=sum(matrix[0])        
imaxcolumn=0
mincolumn=sum(matrix[0])
imincolumn=0
for j in range (m):
    f=0
    for i in range (n):
        f+=matrix[i][j]
    if maxcolumn<f:            #поиск колонки с макс суммой эл
        maxcolumn=f
        imaxcolumn=j
    if mincolumn>f:            #поиск колонки с мин суммой элкмкетов
        mincolumn=f
        imincolumn=j
print ('index of the column with the max sum of elements : ',imaxcolumn)
print ('index of the column with the min sum of elements : ',imincolumn)
print ()
print ('ZEROING THE ELEMENTS ABOVE THE MAIN DIAGONAL : ')
for i in range (n):
    for j in range (m):
        if j>i:
            matrix [i][j]=0
for i in matrix:
    print (i)
print ()
print ('ZEROING THE ELEMENTS BELOW THE MAIN DIAGONAL : ')
for i in range (n):
    for j in range (m):
        if i>j:
            matrix [i][j]=0
for i in matrix:
    print (i)

matrix_a=[]                     #создаем матрицы a и b
matrix_b=[]

for i in range (m):
    matrix_a.append([])
    matrix_b.append([])

for i in range (m):
    for j in range (n):
        matrix_a[i].append(randint(a,b))
        matrix_b[i].append(randint(a,b))

print ()
print ('matrix_a :')
for i in matrix_a:
    print (i)
print ()
print ('matrix_b :')
for i in matrix_b:
    print (i)

print()
print('matrix_c :')
matrix_c=matrix_a                #сумма матриц а и b 
for i in range (m):
    for j in range (n):
        matrix_c[i][j]+=matrix_b[i][j]
for i in matrix_c:
    print (i)



