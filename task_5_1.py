#Написать программу, в которой вводятся два операнда Х и Y и знак операции sign (+, –, /, *). Вычислить результат Z в зависимости от знака. 
#Предусмотреть реакции на возможный неверный знак операции, а также на ввод Y=0 при делении. Организовать возможность многократных вычислений 
#без перезагрузки программа (т.е. построить бесконечный цикл). В качестве символа прекращения вычислений принять ‘0’ (т.е. sign='0').

print ('For exit enter "0" in the sign field. ')
while True:
    x = input('Enter x : ')
    y = input('Enter y : ')
    sign=input('Select sign (+,-,/,*) : ')
    if x.isdigit()==True and y.isdigit() == True:
        x = int(x)
        y = int(y)
    else:
        print ('"x" or "y" not a number ! Try again.')
        continue
    if sign == '+':
        print ('x + y = ',x+y)
    elif sign == '-':
        print ('x - y = ',x-y)
    elif sign == '*':
        print ('x * y = ',x*y)
    elif sign == '/':
        if y != 0:
            print ('x / y = ',x/y)
        else:
            print ('You cannot divide by zero !')
    elif sign != '0':
        print ('Wrong sign ! Try again. ')
        continue
    else:
        print ('Thanks!')
        break
    