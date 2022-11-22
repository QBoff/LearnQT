import sys
from os.path import join

from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QListWidgetItem, QWidget
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt
import sqlite3
from functools import partial


class Pop(QWidget):
    def __init__(self) -> None:
        super().__init__()
        # uic.loadUi(join("QT_Standalone", "task7", "pop.ui"), self)
        uic.loadUi("pop.ui", self)


class MyWidget(QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        # uic.loadUi(join("QT_Standalone", "task7", "prog.ui"), self)
        uic.loadUi("prog.ui", self)
        self.comboBox.addItem("author")
        self.comboBox.addItem("title")
        self.sbtn.clicked.connect(self.search)

    def search(self):
        self.listWidget.clear()
        category = self.comboBox.currentText()
        searchText = self.lineEdit.text()
        # db = sqlite3.connect(join("QT_Standalone", "task7", "books.db"))
        db = sqlite3.connect("books.db")
        cur = db.cursor()
        res = cur.execute(
            f'''SELECT * from books WHERE {category} LIKE "%{searchText}%"''')

        for elem in res:
            # print(elem)
            btn = QPushButton(elem[1], self)

            clickFunc = partial(self.some, elem[1],
                                elem[2], elem[3], elem[4])
            btn.clicked.connect(clickFunc)

            item = QListWidgetItem()
            item.setSizeHint(btn.sizeHint())
            self.listWidget.addItem(item)
            self.listWidget.setItemWidget(item, btn)

    def some(self, name, author, year, genre):
        self.pop = Pop()
        # там снизу есть нужные поля для ввода
        self.pop.preview.setPixmap(QPixmap("cross.png"))
        self.pop.bookAuthor.setText(author)
        self.pop.bookTitle.setText(name)
        self.pop.bookGenre.setText(genre)
        self.pop.bookReleaseYear.setText(str(year))

        self.pop.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    # print(eval("9!"))
    sys.exit(app.exec_())
