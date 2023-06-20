import sys

if __name__ == '__main__':
    s = input('enter the string ').lower()
    a = input('enter 1 character ')
    b = input('enter 2 character ')
    for i in s:
        if i == a or i == b:
            print(i, end='')