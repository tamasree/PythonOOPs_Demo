
class Book:

    def __init__(self, title, author, pages, price):
        self.title = title
        self.author = author
        self.pages = pages
        self.price = price

    #  double-underscore properties are hidden from other classes
        self.__secret = "This is secret"

    # Create instance method

    def getprice(self):
        if hasattr(self, '_discount'):
            return self.price - (self.price * self._discount)
        else:
            return self.price

    def setdiscount(self, amount):
        self._discount = amount


b1 = Book("Title 1", "ABC", 36, 19.20)
print(b1.title)

print(b1.getprice())
b1.setdiscount(0.2)
print(b1.getprice())

print(b1._Book__secret)  # This is called name mangling)
