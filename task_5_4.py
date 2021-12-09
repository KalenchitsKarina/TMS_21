#Для заданного числа N составьте программу вычисления суммы S=1+1/2+1/3+1/4+...+1/N, где N – натуральное число. 

n = input('Enter n : ')
if n.isdigit() == True:
    n = int(n)
    s = 0.0
    if n == 0:
        print('You cannot divide by zero !')
    for i in range (1,n+1):
            s += 1/i    
    print ('sum = ',s)
else:
    print ('n is not a digit')