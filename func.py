import exceptions

def sum (a, b):
    return a + b

def sub (a, b):
    return a - b

def mul (a, b):
    return a * b

def div (a, b):
    return a / b

def my_sign():
        sign = input ('\n+, -, *, /, 0 - exit : ')
        if sign in ['+','-','*','/','0']:
            return sign
        else:
            raise exceptions.WrongSignException

    