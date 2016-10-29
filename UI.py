from PyQt5.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QLineEdit, QListWidget, QListWidgetItem, QLabel, QRadioButton, QCheckBox
from PyQt5.QtCore import QSize, Qt
from PyQt5.QtGui import QIcon, QFont
from Button import Button
from LibraryManager import LibraryManager
from Book import Book

class UI(QWidget):
    def __init__(self, libManager):
        super(UI, self).__init__()

        self.__lib = libManager
        self.__data = []
        self.__listData = []
        self.__item = 0

        self.__ob_widget_add = QWidget()
        self.__ob_widget_delete = QWidget()
        self.__ob_widget_search = QWidget()
        self.__ob_widget_book = QWidget()
        self.__ob_widget_sort = QWidget()

        self.__ob_button_add = Button("Добавить", "res/add.png")
        self.__ob_button_delete = Button("Удалить", "res/delete.png")
        self.__ob_button_search = Button("Поиск", "res/search.png")
        self.__ob_button_sort = Button("Сортировка", "res/sort.png")
        self.__ob_button_add_add = Button("Далее")
        self.__ob_button_delete_yes = Button("Да")
        self.__ob_button_delete_no = Button("Нет")
        self.__ob_button_book_ok = Button("ОК")
        self.__ob_button_sort_ok = Button("Сортировать")

        self.__ob_hlay_main = QHBoxLayout()
        self.__ob_vlay_dock = QVBoxLayout()
        self.__ob_vlay_add = QVBoxLayout()
        self.__ob_vlay_delete = QVBoxLayout()
        self.__ob_hlay_delete = QHBoxLayout()
        self.__ob_vlay_search = QVBoxLayout()
        self.__ob_hlay_search = QHBoxLayout()
        self.__ob_vlay_search_labels = QVBoxLayout()
        self.__ob_vlay_search_lines = QVBoxLayout()
        self.__ob_vlay_book = QVBoxLayout()
        self.__ob_vlay_sort = QVBoxLayout()
        self.__ob_vlay_book_title = QVBoxLayout()
        self.__ob_vlay_book_line = QVBoxLayout()
        self.__ob_hlay_book = QHBoxLayout()
        self.__ob_vlay_sort_widgets = QVBoxLayout()

        self.__ob_label_add = QLabel("<p align='center'><img src='res/add_book.png'><br><br><br>Введите заголовок книги")
        self.__ob_label_delete = QLabel()
        self.__ob_label_search_title = QLabel("Заголовок книги")
        self.__ob_label_search_authors = QLabel("Автор(ы)")
        self.__ob_label_search_isbn = QLabel("Номер ISBN")
        self.__ob_label_search_type = QLabel("Тип книги")
        self.__ob_label_search_year = QLabel("Год издания")
        self.__ob_label_search_icon = QLabel("<p align='center'><img src='res/search_icon.png'><br><br><strong>Поиск")
        self.__ob_label_book = QLabel("<p align='center'><img src='res/about.png'>")
        self.__ob_label_sort = QLabel("<p align='center'><img src='res/sort_icon.png'><br><br><strong>Сортировка")
        self.__ob_label_book_title = QLabel("Заголовок книги")
        self.__ob_label_book_authors = QLabel("Автор(ы)")
        self.__ob_label_book_isbn = QLabel("Номер ISBN")
        self.__ob_label_book_type = QLabel("Тип книги")
        self.__ob_label_book_year = QLabel("Год издания")
        self.__ob_label_book_pages = QLabel("Страниц")
        self.__ob_label_counter = QLabel()

        self.__ob_line_add = QLineEdit()
        self.__ob_line_search_title = QLineEdit()
        self.__ob_line_search_authors = QLineEdit()
        self.__ob_line_search_isbn = QLineEdit()
        self.__ob_line_search_type = QLineEdit()
        self.__ob_line_search_year = QLineEdit()
        self.__ob_line_book_title = QLineEdit()
        self.__ob_line_book_authors = QLineEdit()
        self.__ob_line_book_isbn = QLineEdit()
        self.__ob_line_book_type = QLineEdit()
        self.__ob_line_book_year = QLineEdit()
        self.__ob_line_book_pages = QLineEdit()

        self.__ob_list_main = QListWidget()
        self.__ob_list_search = QListWidget()

        self.__ob_rb_title = QRadioButton("По заголовку книги")
        self.__ob_rb_year = QRadioButton("По году издания")
        self.__ob_rb_pages = QRadioButton("По страницам")

        self.__ob_cb_sort = QCheckBox("По возрастанию")

        # CONFIG;

        self.setLayout(self.__ob_hlay_main)
        self.setMinimumSize(800, 500)
        self.setWindowTitle("Информационно-справочная система 'Библиотека'")

        self.__ob_widget_add.setLayout(self.__ob_vlay_add)
        self.__ob_widget_add.setMinimumSize(400, 400)
        self.__ob_widget_add.setWindowTitle("Добавление книги")
        self.__ob_widget_delete.setLayout(self.__ob_vlay_delete)
        self.__ob_widget_delete.setMinimumSize(400, 300)
        self.__ob_widget_delete.setWindowTitle("Удаление книги")
        self.__ob_widget_search.setWindowTitle("Поиск")
        self.__ob_widget_search.setLayout(self.__ob_vlay_search)
        self.__ob_widget_search.setStyleSheet("background: rgb(250,250,250);")
        self.__ob_widget_search.setMinimumSize(500, 400)
        self.__ob_widget_book.setLayout(self.__ob_vlay_book)
        self.__ob_widget_book.setMinimumSize(400, 300)
        self.__ob_widget_book.setWindowTitle("О книге")
        self.__ob_widget_sort.setLayout(self.__ob_vlay_sort)
        self.__ob_widget_sort.setWindowTitle("Сортировка")
        self.__ob_widget_sort.setMinimumSize(450, 350)

        self.__ob_vlay_dock.addWidget(self.__ob_button_add)
        self.__ob_vlay_dock.addWidget(self.__ob_button_delete)
        self.__ob_vlay_dock.addWidget(self.__ob_button_search)
        self.__ob_vlay_dock.addWidget(self.__ob_button_sort)
        self.__ob_vlay_dock.addWidget(self.__ob_label_counter)
        self.__ob_vlay_dock.setContentsMargins(0, 0, 0, 0)
        self.__ob_vlay_add.addWidget(self.__ob_label_add)
        self.__ob_vlay_add.addWidget(self.__ob_line_add)
        self.__ob_vlay_add.addWidget(self.__ob_button_add_add)
        self.__ob_vlay_add.setContentsMargins(0, 0, 0, 0)
        self.__ob_vlay_delete.addWidget(self.__ob_label_delete)
        self.__ob_vlay_delete.addLayout(self.__ob_hlay_delete)
        self.__ob_vlay_delete.setContentsMargins(0, 0, 0, 0)
        self.__ob_vlay_search.addWidget(self.__ob_label_search_icon)
        self.__ob_vlay_search.addLayout(self.__ob_hlay_search)
        self.__ob_hlay_search.addLayout(self.__ob_vlay_search_labels)
        self.__ob_hlay_search.addLayout(self.__ob_vlay_search_lines)
        self.__ob_vlay_search.addWidget(self.__ob_list_search)
        self.__ob_vlay_search_labels.addWidget(self.__ob_label_search_title)
        self.__ob_vlay_search_labels.addWidget(self.__ob_label_search_authors)
        self.__ob_vlay_search_labels.addWidget(self.__ob_label_search_isbn)
        self.__ob_vlay_search_labels.addWidget(self.__ob_label_search_type)
        self.__ob_vlay_search_labels.addWidget(self.__ob_label_search_year)
        self.__ob_vlay_search_lines.addWidget(self.__ob_line_search_title)
        self.__ob_vlay_search_lines.addWidget(self.__ob_line_search_authors)
        self.__ob_vlay_search_lines.addWidget(self.__ob_line_search_isbn)
        self.__ob_vlay_search_lines.addWidget(self.__ob_line_search_type)
        self.__ob_vlay_search_lines.addWidget(self.__ob_line_search_year)
        self.__ob_hlay_main.setSpacing(0)
        self.__ob_hlay_main.addWidget(self.__ob_list_main, 8)
        self.__ob_hlay_main.addLayout(self.__ob_vlay_dock, 1)
        self.__ob_hlay_main.setContentsMargins(0, 0, 0, 0)
        self.__ob_hlay_delete.addWidget(self.__ob_button_delete_yes)
        self.__ob_hlay_delete.addWidget(self.__ob_button_delete_no)
        self.__ob_hlay_delete.setContentsMargins(0, 0, 0, 0)
        self.__ob_hlay_delete.setSpacing(0)
        self.__ob_vlay_sort.addWidget(self.__ob_label_sort)
        self.__ob_vlay_sort.addLayout(self.__ob_vlay_sort_widgets)
        self.__ob_vlay_sort_widgets.addWidget(self.__ob_rb_title)
        self.__ob_vlay_sort_widgets.addWidget(self.__ob_rb_year)
        self.__ob_vlay_sort_widgets.addWidget(self.__ob_rb_pages)
        self.__ob_vlay_sort_widgets.addWidget(self.__ob_cb_sort)
        self.__ob_vlay_sort.addWidget(self.__ob_button_sort_ok)
        self.__ob_vlay_sort.setContentsMargins(0, 0, 0, 0)
        self.__ob_vlay_sort_widgets.setContentsMargins(5, 0, 5, 0)
        self.__ob_vlay_book.addWidget(self.__ob_label_book)
        self.__ob_vlay_book.addLayout(self.__ob_hlay_book)
        self.__ob_vlay_book.addWidget(self.__ob_button_book_ok)
        self.__ob_vlay_book.setContentsMargins(0, 0, 0, 0)
        self.__ob_hlay_book.addLayout(self.__ob_vlay_book_title)
        self.__ob_hlay_book.addLayout(self.__ob_vlay_book_line)
        self.__ob_vlay_book_title.addWidget(self.__ob_label_book_title)
        self.__ob_vlay_book_title.addWidget(self.__ob_label_book_authors)
        self.__ob_vlay_book_title.addWidget(self.__ob_label_book_isbn)
        self.__ob_vlay_book_title.addWidget(self.__ob_label_book_type)
        self.__ob_vlay_book_title.addWidget(self.__ob_label_book_pages)
        self.__ob_vlay_book_title.addWidget(self.__ob_label_book_year)
        self.__ob_vlay_book_line.addWidget(self.__ob_line_book_title)
        self.__ob_vlay_book_line.addWidget(self.__ob_line_book_authors)
        self.__ob_vlay_book_line.addWidget(self.__ob_line_book_isbn)
        self.__ob_vlay_book_line.addWidget(self.__ob_line_book_type)
        self.__ob_vlay_book_line.addWidget(self.__ob_line_book_pages)
        self.__ob_vlay_book_line.addWidget(self.__ob_line_book_year)
        self.__ob_vlay_book_title.setContentsMargins(5, 0, 0, 0)
        self.__ob_vlay_book_line.setContentsMargins(0, 0, 5, 0)

        self.__ob_button_add.clicked.connect(self.__onAdd)
        self.__ob_button_add_add.setFixedHeight(70)
        self.__ob_button_add_add.clicked.connect(self.__onAddingBook)
        self.__ob_button_delete.clicked.connect(self.__onDeleteBook)
        self.__ob_button_delete_yes.setFixedHeight(40)
        self.__ob_button_delete_no.setFixedHeight(40)
        self.__ob_button_delete_no.clicked.connect(self.__ob_widget_delete.hide)
        self.__ob_button_delete_yes.clicked.connect(self.__onDeleteBookYes)
        self.__ob_button_search.clicked.connect(self.__ob_widget_search.show)
        self.__ob_button_book_ok.clicked.connect(self.__onCloseAboutBook)
        self.__ob_button_book_ok.setFixedHeight(40)
        self.__ob_button_sort_ok.setFixedHeight(40)
        self.__ob_button_sort.clicked.connect(self.__ob_widget_sort.show)
        self.__ob_button_sort_ok.clicked.connect(self.__onSort)

        self.__ob_line_add.setStyleSheet("border: none; background: rgb(200,200,200)")
        self.__ob_line_add.setFixedHeight(40)
        self.__ob_line_add.setAlignment(Qt.AlignCenter)
        self.__ob_line_search_title.setStyleSheet(self.__ob_line_add.styleSheet())
        self.__ob_line_search_authors.setStyleSheet(self.__ob_line_add.styleSheet())
        self.__ob_line_search_isbn.setStyleSheet(self.__ob_line_add.styleSheet())
        self.__ob_line_search_type.setStyleSheet(self.__ob_line_add.styleSheet())
        self.__ob_line_search_year.setStyleSheet(self.__ob_line_add.styleSheet())
        self.__ob_line_search_title.textChanged.connect(self.__onSearchLineEdit)
        self.__ob_line_search_authors.textChanged.connect(self.__onSearchLineEdit)
        self.__ob_line_search_type.textChanged.connect(self.__onSearchLineEdit)
        self.__ob_line_search_isbn.textChanged.connect(self.__onSearchLineEdit)
        self.__ob_line_search_year.textChanged.connect(self.__onSearchLineEdit)
        self.__ob_line_book_title.setStyleSheet(self.__ob_line_add.styleSheet())
        self.__ob_line_book_authors.setStyleSheet(self.__ob_line_add.styleSheet())
        self.__ob_line_book_isbn.setStyleSheet(self.__ob_line_add.styleSheet())
        self.__ob_line_book_type.setStyleSheet(self.__ob_line_add.styleSheet())
        self.__ob_line_book_pages.setStyleSheet(self.__ob_line_add.styleSheet())
        self.__ob_line_book_year.setStyleSheet(self.__ob_line_add.styleSheet())

        self.__ob_label_delete.setAlignment(Qt.AlignCenter)
        self.__ob_label_search_title.setAlignment(Qt.AlignRight)
        self.__ob_label_search_authors.setAlignment(Qt.AlignRight)
        self.__ob_label_search_isbn.setAlignment(Qt.AlignRight)
        self.__ob_label_search_type.setAlignment(Qt.AlignRight)
        self.__ob_label_search_year.setAlignment(Qt.AlignRight)
        self.__ob_label_book.setFont(QFont("Arial", 11))
        self.__ob_label_counter.setStyleSheet("background-color: rgb(23,116,173); color: white;")
        self.__ob_label_counter.setAlignment(Qt.AlignCenter)
        self.__ob_label_counter.setFixedHeight(40)

        self.__ob_cb_sort.setChecked(True)

        self.__ob_rb_title.setChecked(True)

        self.__ob_list_main.setStyleSheet("QListWidget {border: none;} QListWidget::item:selected { background:"
                                          "rgb(23,136,150); }")
        self.__ob_list_main.setSelectionMode(QListWidget.MultiSelection)
        self.__ob_list_main.doubleClicked.connect(self.__onDoubleClickItem)
        self.__ob_list_search.doubleClicked.connect(self.__onDoubleClickItem)
        self.__ob_list_search.setStyleSheet("QListWidget::item:selected { background:"
                                          "rgb(23,136,150); }")
        self.loadBooks()

    def loadBooks(self):
        self.__ob_list_main.clear()
        for book in self.__lib.getItems():
            item = QListWidgetItem()
            item.setText(book.title+"\nАвтор(ы): "+str(book.authors)+", "+str(book.year)+" год.")
            item.setSizeHint(QSize(200, 50))
            item.setIcon(QIcon("res/book.png"))
            item.setFont(QFont("Arial", 13))
            self.__ob_list_main.addItem(item)

        self.__ob_label_counter.setText("Книг: "+str(self.__ob_list_main.count()))

    def __onAdd(self):
        self.__ob_widget_add.show()

    def __onAddingBook(self):
        if(len(self.__data) == 0):
            if(self.__ob_line_add.text() != ""  and not self.__ob_line_add.text().isdigit()):
                self.__data.append(self.__ob_line_add.text())
                self.__ob_label_add.setText("<p align='center'><img src='res/author.png'><br><br><br>Введите "
                                            "автора(ов) книги")
        elif(len(self.__data) == 1):
            if(self.__ob_line_add.text() != "" and not self.__ob_line_add.text().isdigit()):
                self.__data.append(self.__ob_line_add.text())
                self.__ob_label_add.setText(
                    "<p align='center'><img src='res/isbn.png'><br><br><br>Введите номер ISBN")
        elif(len(self.__data) == 2):
            if (self.__ob_line_add.text() != "" and self.__ob_line_add.text().isdigit() and int(self.__ob_line_add.text()) > 0):
                self.__data.append(self.__ob_line_add.text())
                self.__ob_label_add.setText(
                    "<p align='center'><img src='res/type.png'><br><br><br>Введите тип книги")
        elif(len(self.__data) == 3):
            if (self.__ob_line_add.text() != "" and not self.__ob_line_add.text().isdigit()):
                self.__data.append(self.__ob_line_add.text())
                self.__ob_label_add.setText(
                    "<p align='center'><img src='res/pages.png'><br><br><br>Введите количество страниц")
        elif(len(self.__data) == 4):
            if (self.__ob_line_add.text() != "" and self.__ob_line_add.text().isdigit() and int(self.__ob_line_add.text()) > 0):
                self.__data.append(self.__ob_line_add.text())
                self.__ob_label_add.setText(
                    "<p align='center'><img src='res/year.png'><br><br><br>Введите год издания")
        elif(len(self.__data) == 5):
            if (self.__ob_line_add.text() != "" and self.__ob_line_add.text().isdigit() and int(self.__ob_line_add.text()) > 0):
                self.__data.append(self.__ob_line_add.text())
                self.__lib.addItem(self.__data)
                self.__ob_label_add.setText("<p align='center'><img src='res/added.png'>"
                                            "<br><br><br>Книга добавлена!")
                self.__ob_line_add.hide()
                self.__ob_button_add_add.setCurrentText("ОК")
        elif(len(self.__data) == 6):
            self.__data.clear()
            self.__ob_list_main.clear()
            self.loadBooks()
            self.__ob_button_add_add.setCurrentText("Далее")
            self.__ob_label_add.setText(
                "<p align='center'><img src='res/add_book.png'><br><br><br>Введите заголовок книги")
            self.__ob_widget_add.close()
            self.__ob_line_add.show()
        self.__ob_line_add.clear()

    def __onDeleteBook(self):
        self.__ob_widget_delete.show()
        if(len(self.__ob_list_main.selectedItems()) != 0):
            self.__ob_button_delete_yes.show()
            self.__ob_button_delete_no.setCurrentText("Нет")
            self.__ob_label_delete.setText("<p align='center'><img src='res/delete_book.png'><br><br><br>Удалить? ("+str(len(self.__ob_list_main.selectedItems()))+")")
        else:
            self.__ob_button_delete_yes.hide()
            self.__ob_button_delete_no.setCurrentText("ОК")
            self.__ob_label_delete.setText("<p align='center'><img src='res/delete_book.png'><br><br><br>Не выбрано книг для удаления")

    def __onDeleteBookYes(self):
        for item in self.__ob_list_main.selectedItems():
            self.__lib.deleteItem(self.__ob_list_main.row(item))
        self.loadBooks()
        self.__ob_widget_delete.close()

    def __onSearchLineEdit(self):

        counter = 0
        counter_iter = 0
        self.__ob_list_search.clear()
        self.__listData.clear()

        if(len(self.__ob_line_search_title.text()) != 0):
            counter += 1
        if (len(self.__ob_line_search_authors.text()) != 0):
            counter += 1
        if (len(self.__ob_line_search_isbn.text()) != 0):
            counter += 1
        if (len(self.__ob_line_search_type.text()) != 0):
            counter += 1
        if (len(self.__ob_line_search_year.text()) != 0):
            counter += 1

        for item in self.__lib.getItems():
            if(len(self.__ob_line_search_title.text()) != 0 and self.__ob_line_search_title.text().upper() in item.title.upper()):
                counter_iter += 1
            if (len(self.__ob_line_search_authors.text()) != 0 and self.__ob_line_search_authors.text().upper() in item.authors.upper()):
                counter_iter += 1
            if (len(self.__ob_line_search_type.text()) != 0 and self.__ob_line_search_type.text().upper() in item.type.upper()):
                counter_iter += 1
            if (len(self.__ob_line_search_year.text()) != 0 and self.__ob_line_search_year.text().isdigit() and
                        item.year == int(self.__ob_line_search_year.text())):
                counter_iter += 1
            if (len(
                    self.__ob_line_search_isbn.text()) != 0 and self.__ob_line_search_isbn.text().isdigit() and item.isbn == int(
                    self.__ob_line_search_isbn.text())):
                counter_iter += 1
            if(counter_iter == counter and counter != 0):
                self.__listData.append(item)
                self.__ob_list_search.show()
                book = QListWidgetItem()
                book.setText(item.title + "\nАвтор(ы): " + str(item.authors) + ", " + str(item.year) + " год.")
                book.setSizeHint(QSize(200, 50))
                book.setIcon(QIcon("res/book.png"))
                book.setFont(QFont("Arial", 13))
                self.__ob_list_search.addItem(book)
            counter_iter = 0

    def __onDoubleClickItem(self):

        if(self.sender() == self.__ob_list_main):
            self.__item = self.__lib.getItems()[self.__ob_list_main.row(self.__ob_list_main.currentItem())]
        else:
            self.__item = self.__listData[self.__ob_list_search.row(self.__ob_list_search.currentItem())]

        self.__ob_line_book_title.setText(self.__item.title)
        self.__ob_line_book_authors.setText(self.__item.authors)
        self.__ob_line_book_isbn.setText(str(self.__item.isbn))
        self.__ob_line_book_type.setText(self.__item.type)
        self.__ob_line_book_pages.setText(str(self.__item.pages))
        self.__ob_line_book_year.setText(str(self.__item.year))

        self.__ob_widget_book.show()

    def __onSort(self):
        data = []
        new_list = []

        if(self.__ob_rb_title.isChecked()):
            for item in self.__lib.getItems():
                data.append(item.title)
            data.sort(reverse=not self.__ob_cb_sort.isChecked())
            for i in data:
                for book in self.__lib.getItems():
                    if(i == book.title):
                        new_list.append(book)
                        break

        if (self.__ob_rb_pages.isChecked()):
            for item in self.__lib.getItems():
                data.append(item.pages)
            data.sort(reverse=not self.__ob_cb_sort.isChecked())
            for i in data:
                for book in self.__lib.getItems():
                    if (i == book.pages):
                        new_list.append(book)
                        break

        if (self.__ob_rb_year.isChecked()):
            for item in self.__lib.getItems():
                data.append(item.year)
            data.sort(reverse=not self.__ob_cb_sort.isChecked())
            for i in data:
                for book in self.__lib.getItems():
                    if (i == book.year):
                        new_list.append(book)
                        break

        self.__lib.replace(new_list)
        self.loadBooks()
        self.__ob_widget_sort.close()

    def __onCloseAboutBook(self):
        if(len(self.__ob_line_book_title.text()) != 0 and not self.__ob_line_book_title.text().isdigit()):
            self.__item.title = self.__ob_line_book_title.text()
        if (len(self.__ob_line_book_authors.text()) != 0 and not self.__ob_line_book_authors.text().isdigit()):
            self.__item.authors = self.__ob_line_book_authors.text()

        if(len(self.__ob_line_book_isbn.text()) != 0 and self.__ob_line_book_isbn.text().isdigit() and int(self.__ob_line_book_isbn.text()) > 0):
            self.__item.isbn = int(self.__ob_line_book_isbn.text())

        if (len(self.__ob_line_book_type.text()) != 0 and self.__ob_line_book_type.text().isalpha()):
            self.__item.type = self.__ob_line_book_type.text()

        if (len(self.__ob_line_book_pages.text()) != 0 and self.__ob_line_book_pages.text().isdigit() and int(self.__ob_line_book_pages.text()) > 0):
            self.__item.pages = int(self.__ob_line_book_pages.text())

        if (len(self.__ob_line_book_year.text()) != 0 and self.__ob_line_book_year.text().isdigit() and int(self.__ob_line_book_year.text()) > 0):
            self.__item.year = int(self.__ob_line_book_year.text())

        self.loadBooks()
        self.__ob_widget_book.hide()
