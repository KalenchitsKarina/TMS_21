from abc import abstractmethod
import math

class Point:

    def __init__ (self, x, y):
        self._x = x
        self._y = y

class Figure:
    
    @abstractmethod
    def perimetr():
        return NotImplemented

    @abstractmethod
    def ploshchad():
        return NotImplemented

    @abstractmethod
    def dlina():
        return NotImplemented

class Circle (Point, Figure):

    def __init__(self, x, y, len):
        super().__init__(x, y)
        self._len = len

    def perimetr(self):
        return (2 * math.pi * self._len) 

    def ploshchad(self):
        return (self._len ** 2 * math.pi) 

class Triangle (Point, Figure):
    
    def __init__(self, x, y, x2, y2, x3, y3):
        super().__init__(x, y)
        super().__init__(x2,y2)
        super().__init__(x3,y3)
        self._a = (math.sqrt(math.pow((x - x2),2) + (y - y2)**2))
        self._b = (math.sqrt((x2 - x3)**2 + (y2 - y3)**2))
        self._c = (math.sqrt((x3 - x)**2 + (y3 - y)**2))

    def perimetr(self) -> float:
        return self._a + self._b + self._c

    def ploshchad(self) -> float:
        p = (self._a + self._b + self._c )/ 2
        return math.sqrt(p * (p - self._a) * (p - self._b) * (p - self._c))

class Square (Point, Figure):

    def __init__(self, x, y, x2, y2):
        super().__init__(x, y)
        super().__init__(x2, y2)
        self._a = (math.sqrt(math.pow((x - x2),2) + math.pow((y - y2),2)))

    def perimetr(self) -> float:
        return self._a * 4

    def ploshchad(self) -> float:
        return self._a ** 2

    
