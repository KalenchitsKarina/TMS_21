def decorator_reverse_arg(f):
    def wrapper(*args):
        args1 = [args[i] for i in range(len(args))]
        args1.reverse()
        result = f (*args1)
        return result
    return wrapper

@decorator_reverse_arg
def sum (a,b,c):
    return a+b+c

@decorator_reverse_arg
def delete (a,b):
    return a/b

def main():
    print (sum(' Hello',' world','map'))
    print (sum('ник','ор','вт'))
    print (delete (2,4))
if __name__ == "__main__":
    main()



