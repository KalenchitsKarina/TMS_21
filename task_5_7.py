from random import randint
while True:
    n = input('Enter size of matrix : ')
    if n.isdigit() == True:
        n = int(n)
        break
    else:
        print('n is not digit! Try again! ')
        
matrix = [[randint(1,20) for j in range (n)] for i in range (n)]

for i in matrix:
    print (i)
print()

for i in range(n):
    max = matrix[0][0]
    for j in range (n):            #находим максимальный элемент в строке и его индекс
        if matrix[i][j] > max:
            max = matrix[i][j]
            ind = j
    for j in range (n):            #меняем наибольший элемент с элементом на главной диагонали
        if i == j:      
            p = matrix[i][j]
            matrix[i][j] = max
            matrix[i][ind] = p       
for i in matrix:
    print (i)

