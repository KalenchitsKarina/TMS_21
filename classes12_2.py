from abc import ABC, abstractmethod

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
        return 2 * 3.14 * self._len

    def ploshchad(self):
        return self._len ^ 2 * 3.14

class Triangle (Point, Figure):
    
    def __init__(self, x, y, x2, y2, x3, y3):
        super().__init__(x, y)
        super().__init__(x2, y2)
        super().__init__(x3, y3)

    def dlina(self, a, b, a2, b2, a3, b3) -> list : 
        ls = []
        ls.append(0.5 ** ((a - a2)**2 + (b-b2)**2))
        ls.append(0.5 ** ((a2 - a3)**2 + (b2-b3)**2))
        ls.append(0.5 ** ((a3 - a)**2 + (b3-b)**2))
        return ls

    def perimetr(self, a, b, a2, b2, a3, b3):
        pass


class Square (Point, Figure):

    def __init__(self, x, y, x2, y2):
        super().__init__(x, y)
        super().__init__(x2, y2)
