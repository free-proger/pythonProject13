import sys

if __name__ == '__main__':
    s = input('enter the string ').lower()
    if s.count('чя')>0 or s.count('щя')>0:
        print('ча ща пиши с буквой а!')
    else:
        print('все правильно написал!')