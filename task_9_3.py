def decorator_del_chet(f):
    def wrapper (a:list):
        b = [a[i] for i in range (len(a)) if a[i]%2 != 0]
        result = f(b)
        return result
    return wrapper

@decorator_del_chet
def func (a:list): 
        return a

def main():
    print(func([2,4,3,5,6,7,22,34,31,5,81,12]))
if __name__ == "__main__":
    main()