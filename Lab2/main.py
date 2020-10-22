# coding=utf-8
# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


from lab_python_oop.Rectangle import Rectangle
from lab_python_oop.Circle import Circle
from lab_python_oop.Square import Square
#import arrow


def main():
    print("ИУ5-51Б Пахомкин Кирсан Лаб №2")
    #print(arrow.now(), "\n")

    rectangle = Rectangle("синего", 16, 16)
    circle = Circle("зеленого", 16)
    square = Square("красного", 16)

    print(rectangle)
    print(circle)
    print(square)


if __name__ == "__main__":
    main()