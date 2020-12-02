#!/usr/bin/evn python3
# -*- config: utf-8 -*-

if __name__ == '__main__':
    a = int(input('Введите целое число: '))

    def rand():
        if a >= 0:
            positive()
        elif a < 0:
            negative()

    def positive():
        print('Положительное')

    def negative():
        print('Отрицательное')

    rand()
