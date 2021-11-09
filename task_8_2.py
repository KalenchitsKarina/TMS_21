def is_palindrom(a:str):
    if a == a[::-1]:
        print (a,"- палиндром")
    else:
        print (a,'не является палиндромом')

def main():
    for i in range (3):
        word = input('Enter word : ')
        is_palindrom(word)

if __name__ == "__main__":
    main()