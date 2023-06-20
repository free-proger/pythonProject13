import sys

if __name__ == '__main__':
    s = input('enter the string ').lower()
    a = input('enter character ').lower()
    s=s[:s.rfind('и')]+a+s[s.rfind('и'):]
    print(s)