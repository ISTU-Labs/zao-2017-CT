#!/usr/bin/python

# + Сверхпростой синтаксис
# + Богатейшая библиотека
# + Синтаксис языка позвояет его делать языком управления сложными приложениями.
# + Возможность расширения функций прграммами на С.

# - Производительность. Прим в 10 раз медл. Java.
# - Глобальная блокировка потоков.
# print("Hello, World!")


def fact(x: int):
    assert x >= 0
    if x in [0, 1]:
        return 1
    else:
        return x * fact(x - 1)


def main():
    L = [1, 2, 3, 10]

    L1 = []

    for e in L:
        L1.append(fact(e))

    L2 = list(map(fact, L))

    L3 = [fact(e) for e in L if e >= 3]

    print(L3)

    t = (1, 2, 3, 4)

    print(t[0], L3[0], len(t), len(L3))

    d = {1: "one", 2: "two", 3: "three"}

    rd = {v: k for k, v in d.items()}

    print(d[1], rd["one"])
    print(rd)

    # private:
    #     char * m_name;


class Animal(object):
    def __init__(self, name):
        self.name = name

    def say(self):
        raise RuntimeError("should be implemented by subclass")

    def __str__(self):
        return "{}:{}".format(
            self.name,
            self.__class__.__name__
        )


class Cat(Animal):
    def say(self):
        print("Мяу")


class Dog(Animal):
    def say(self):
        print("Гав")


# google: julia lang
# google: learnxinyminits.com
