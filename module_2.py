#!/usr/bin/evn python3
# -*- config: utf-8 -*-

import math


def cylinder(r, h, full=True):
    def circle(r):
        return math.pi * (r ** 2)

    s_cylinder = 2 * math.pi * r * h

    if full:
        return s_cylinder + 2 * circle(r)
    else:
        print(s_cylinder)


if __name__ == '__main__':
    s_circle = 0
    a = float(input("Введите радиус: "))
    b = float(input("Введите высоту: "))

    c = input("side or full?")
    s = cylinder(a, b, full=(c == 'full'))
    print(s)