import exceptions
class Math:
    def __init__(self, a, b):
        self._a = a
        self._b = b

    def sum (self):
        return self._a + self._b

    def sub (self):
        return self._a - self._b

    def mul (self):
        return self._a * self._b

    def div (self):
        return self._a / self._b

    def my_sign():
            sign = input ('\n+, -, *, /, 0 - exit : ')
            if sign in ['+','-','*','/','0']:
                return sign
            else:
                raise exceptions.WrongSignException

    