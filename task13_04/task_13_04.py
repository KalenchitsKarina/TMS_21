class Book:
    def __init__(self, pages :int, year :int, author :str, price :int) -> None:
        self.__pages = pages
        self.__year = year
        self.__author = author
        self.__price = price

    


class WrongType (Exception):
    def __init__(self, message='Wrong type'):
       super().__init__(message)
raise WrongType

class WrongTypeNeedStr (WrongType):
    
 
