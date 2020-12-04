#!/usr/bin/evn python3
# -*- config: utf-8 -*-


def rand(a):
    if a >= 0:
        positive(a)
    elif a < 0:
        negative(a)


def positive(a):
    print('Положительное')


def negative(a):
    print('Отрицательное')


if __name__ == '__main__':
    a = int(input('Введите целое число: '))

    rand(a)
