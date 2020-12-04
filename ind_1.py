#!/usr/bin/env python3
# -*- config: utf-8 -*-

# Вариант 12. Использовать словарь, содержащий следующие ключи: фамилия, имя; номер телефона;
# дата рождения (список из трех чисел). Написать программу, выполняющую следующие
# действия: ввод с клавиатуры данных в список, состоящий из словарей заданной структуры;
# записи должны быть размещены по алфавиту; вывод на экран информации о людях, чьи
# дни рождения приходятся на месяц, значение которого введено с клавиатуры; если таких
# нет, выдать на дисплей соответствующее сообщение.

from datetime import date
import sys
import json
import xml.etree.ElementTree as ET


def f_add(person, name, phone, birthday):

    if 1 >= birthday[1] > 12:
        print("Такого месяца не существует!", file=sys.stderr)
        exit(1)

    if 1 >= birthday[0] > 31:
        print("Такого дня не существует!", file=sys.stderr)
        exit(1)

    today = date.today()
    if birthday[2] > today.year:
        print(f"{birthday[2]} ещё не наступил!", file=sys.stderr)
        exit(1)

    person = {
        'name': name,
        'phone': phone,
        'birthday': birthday,
    }

    people.append(person)
    if len(people) > 1:
        people.sort(key=lambda item: item.get('name', ''))


def f_list(people):
    table = []
    line = '+-{}-+-{}-+-{}-+-{}-+-{}-+-{}-+'.format(
        '-' * 4,
        '-' * 30,
        '-' * 20,
        '-' * 8,
        '-' * 8,
        '-' * 8
    )
    table.append(line)
    table.append(
        '| {:^3} | {:^30} | {:^20} | {:^8} | {:^8} | {:^8} |'.format(
            "№",
            "ФИО",
            "Номер телефона",
            "День",
            "Месяц",
            "Год"
        )
    )
    table.append(line)

    for idx, person in enumerate(people, 1):
        table.append(
            '| {:>4} | {:<30} | {:<20} | {:>8} | {:>8} | {:>8} |'.format(
                idx,
                person.get('name', ''),
                person.get('phone', ''),
                person.get('birthday[0]', ''),
                person.get('birthday[1]', ''),
                person.get('birthday[2]', '')
            )
        )
    table.append(line)

    return '\n'.join(table)


def f_select():
    parts = command.split(' ', maxsplit=2)
    month = int(parts[1])

    count = 0
    for person in people:
        birthday = person.get('birthday', [])
        if birthday:
            if birthday[1] == month:
                count += 1
                print(f'{count}, {person.get("name", "")}')

    if count == 0:
        print(f"Именинников в {month} месяце нетю :(")


def f_load():
    parts = command.split(' ', maxsplit=1)

    if 'xml' in parts[1]:
        print('здесь должна быть магия')
    elif 'json' in parts[1]:
        with open(parts[1], 'r') as f:
            people = json.load(f)
            return people


def f_save():
    parts = command.split(' ', maxsplit=1)

    if 'xml' in parts[1]:
        print('здесь должна быть магия')
    elif 'json' in parts[1]:
        with open(parts[1], 'w')as f:
            json.dump(people, f)


def f_help():
    print("Список команд:\n")
    print("add - добавить человека;")
    print("list - вывести список людей;")
    print("select <месяц рождения> - дни рождения в текущем месяце;")
    print("load <имя файла> - загрузить данные из файла;")
    print("save <имя файла> - сохранить данные в файл;")
    print("help - отобразить справку;")
    print("exit - завершить работу с программой.")


def f_err():
    print(f"Неизвестная команда {command}", file=sys.stderr)


if __name__ == '__main__':
    people = []

    while True:
        command = input(">>> ").lower()

        if command == 'exit':
            break

        elif command == 'add':
            name = input("Фамилия, Имя ")
            phone = input("Номер телефона ")
            birthday = list(map(int, input("Дата рождения в формате: дд,мм,гггг ").split(',')))

            f_add(people, name, phone, birthday)

        elif command == 'list':
            print(f_list(people))

        elif command.startswith('select '):
            f_select()

        elif command.startswith('load '):
            people = f_load()

        elif command.startswith('save '):
            f_save()

        elif command == 'help':
            f_help()

        else:
            f_err()
