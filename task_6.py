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

for i in matrix:
    print (i)

max=0
for i in range (n):
    for j in range (m):
        if matrix[i][j]>max:
            max=matrix[i][j]
print ('maximum matrix element : ',max )

