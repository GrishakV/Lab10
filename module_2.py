#!/usr/bin/evn python3
# -*- config: utf-8 -*-

import math


def cylinder(r, h):
    def circle():
        result = side + 2 * (math.pi * r ** 2)
        return result

    side = 2 * math.pi * r * h

    a = input('Получить площадь полностью? да/нет ')

    if a == 'да':
        circle()
        full = circle()
        print(full)

    elif a == 'нет':
        print(side)


if __name__ == '__main__':
    x = int(input('Введите высоту: '))
    y = int(input('Введите радиус: '))

    cylinder(x, y)
