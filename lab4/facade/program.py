

from facade.library import LibraryOperator

operator = LibraryOperator()

def orderBook(nameBook, adress):
    return operator.callUp(nameBook, adress)


if __name__ == '__main__':
    print(orderBook("Kniga", "address"))
