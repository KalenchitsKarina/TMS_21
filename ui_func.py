from exceptions import WrongSignException
from func import my_sign
from func import sum
from func import sub
from func import mul
from func import div

def run():

    print ('''_____________________\n
      СALCULATOR''')

    while True:
        print ('_____________________')
        try:
            sign = my_sign()
        except WrongSignException:
            print ('Wrong sign!')
            continue
        
        if sign == '0':
            break
        try:
            a = int (input('Enter a : '))
            b = int (input('Enter b : '))
        except ValueError:
            print ('Invalid input type. You should enter numbers.')
            continue
        if sign == '+':
            result = sum(a, b)
        elif sign == '-':
            result = sub(a, b)
        elif sign == '*':
            result = mul(a, b)
        elif sign == '/':
            try:
                result = div (a, b)
            except ZeroDivisionError:
                print ('division by zero.')
                continue
        try:
            print (f'result = {result}')
        except UnboundLocalError:
            print ('result = None')
            

