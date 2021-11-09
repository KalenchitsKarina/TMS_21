import random
import math

def Sin1(x:float,eps:float):
    if eps <= 0:
        print("Epsilon should be greater than 0")
    y = x
    f = x
    i = 3
    while abs(y) > eps:
        y *= (-1) * x * x / ((i-1)*i)
        i += 2
        f += y
    return f


def main ():
    eps = 0.01
    for i in range(0, 6):
        #x = -0.5
        #x = 2
        x = math.pi / 4
        print("eps = ", eps, "; sin(",x,") = ",Sin1(x,eps),";",math.sin(x))
        eps /= 10
if __name__ == "__name__":
    main()
