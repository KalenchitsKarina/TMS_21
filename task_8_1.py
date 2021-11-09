def fact2(n:int) ->int:
    if n % 2 == 0:
        fact = 1
        for i in range(2,n+1,2):
            fact *= i
        return fact
    else:
        fact = 1
        for i in range (1,n+1,2):
            fact *= i
        return fact

def main():
    for i in range (5):
        a = int(input('Enter n : '))
        print ('n!! = ',fact2(a))

if __name__ == "__main__":
    main()