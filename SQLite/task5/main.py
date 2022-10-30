import sqlite3
import sys

from PyQt5 import uic
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *


class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("SQLite/task5/prog.ui", self)

        self.db = sqlite3.connect("SQLite/task5/films_db.sqlite")
        self.c = self.db.cursor()
        self.searching = "year"

        self.comboBox.addItems([
            "Год выпуска",
            "Название",
            "Продолжительность"
        ])

        self.search.clicked.connect(self.searchInDb)
        self.comboBox.activated[str].connect(self.onActivated)

    def searchInDb(self):
        try:
            text = self.param.text()
            if text == '':
                raise ValueError

            cur = self.c
            queue = "SELECT films.id, films.title, films.year, films.genre, films.duration FROM films WHERE " + \
                self.searching + ' = ?'
            res = cur.execute(queue, (text,)).fetchone()
            self.id.setText(str(res[0]))
            self.name.setText(str(res[1]))
            self.year.setText(str(res[2]))
            self.genre.setText(str(res[3]))
            self.duration.setText(str(res[4]))

        except ValueError:
            self.error.setText("Введите нормалные данные")
        except Exception as e:
            self.error.setText("Ничего не найдено")

    def onActivated(self, text):
        if text == 'Год выпуска':
            self.searching = 'year'
        elif text == 'Название':
            self.searching = 'title'
        elif text == 'Продолжительность':
            self.searching = 'duration'


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()

    sys.exit(app.exec_())
