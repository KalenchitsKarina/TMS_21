from classes import Circle
from classes import Triangle
from classes import Square
def main():
    
    ls_f = []
    ls_f.append(Circle(1,1,3))
    ls_f.append(Triangle (1,1,5,1,1,4))
    ls_f.append(Square (1,1,6,1))

    for i in ls_f:
        print (f'p = {i.perimetr()}')
        print (f's = {i.ploshchad()}')

if __name__ == "__main__":
    main()