# Итератор для удаления дубликатов
from gen_random import gen_random


class Unique:
    """Итератор, оставляющий только уникальные значения."""

    def __init__(self, data, **kwargs):
        self.used_elements = set()
        self.data = data
        self.index = 0
        self.ignore_case = False
        if 'ignore_case' in kwargs.keys():
            self.ignore_case = kwargs['ignore_case']

    def __iter__(self):
        return self

    def __next__(self):
        while True:
            if self.index >= len(self.data):
                raise StopIteration
            else:
                current = self.data[self.index]
                self.index = self.index + 1
                if self.ignore_case:
                    if current.upper() not in self.used_elements:
                        # Добавление в множество производится
                        # с помощью метода add
                        self.used_elements.add(current.upper())
                        return current
                else:
                    if current not in self.used_elements:
                        # Добавление в множество производится
                        # с помощью метода add
                        self.used_elements.add(current)
                        return current


def uniqueSort(arr):
    tmp = []
    for i in Unique(arr, ignore_case=True):
        tmp.append(i)
    return sorted(tmp)


# for i in Unique(["abc", "dsada", "dSada", "abc"], ignore_case=True):
#     print(i, end=" ")
# print()
# for i in Unique(gen_random(7, 1, 3)):
#     print(i, end=" ")
# print()
# for i in Unique([1, 6, 4, 3, 6, 4, 3, 2, 76, 3, 23, 4]):
#     print(i, end=" ")
# print()