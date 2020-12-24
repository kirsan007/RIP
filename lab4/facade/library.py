

class Librarian():
    def findBook(self, nameBook):
        pass
    def handoverBook(self):
        pass

class Delivery():
    adress = None
    nameBook = None

    def cometoOrder(self):
        pass
    def getOrder(self, nameBook):
        self.nameBook = nameBook
    def deliveryOrder(self, adress):
        self.adress = adress

class LibraryOperator():
    i = 0
    def isBookAvailable(self, nameBook):
        self.i = self.i + 1
        if self.i % 2 == 1:
            return True
        else:
            return False

    def callUp(self, nameBook, adress):
        if not self.isBookAvailable(nameBook):
            return {
                "success": False
            }
        librarian = Librarian()
        delivery = Delivery()

        librarian.findBook(nameBook)
        delivery.cometoOrder()
        delivery.getOrder(nameBook)
        librarian.handoverBook()
        delivery.deliveryOrder(adress)
        return {
            "success": True,
            "delivery": delivery
        }




