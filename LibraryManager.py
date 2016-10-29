from pickle import dump, load
from Book import Book


class LibraryManager:
    def __init__(self):

        self.__items = []
        self.__path = "Books"

        self.loadData()

    def getItems(self):
        return self.__items

    def loadData(self):
        try:
            file = open(self.__path, "rb")
            self.__items = load(file)
            file.close()
        except:
            pass

    def dumpData(self):
        file = open(self.__path, "wb")
        dump(self.__items, file)
        file.close()

    def addItem(self, data):
        item = Book()
        item.title = data[0]
        item.authors = data[1]
        item.isbn = int(data[2])
        item.type = data[3]
        item.pages = int(data[4])
        item.year = int(data[5])
        self.__items.append(item)
        self.dumpData()

    def deleteItem(self, item):
        self.__items.remove(self.__items[item])
        self.dumpData()

    def replace(self, new):
        if(type(new) == list):
            self.__items = new
            self.dumpData()
