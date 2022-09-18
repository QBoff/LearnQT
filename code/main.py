import sys

from PyQt5.QtWidgets import *


class Example(QWidget):
    def __init__(self):
        super().__init__()

        # elements of out design
        self.eq = QPushButton("=", self)
        self.point = QPushButton(".", self)
        self.CE = QPushButton("CE", self)
        self.zero = QPushButton("0", self)
        self.C = QPushButton("C", self)
        self.plus = QPushButton("+", self)
        self.minus = QPushButton("-", self)
        self.umnosh = None
        self.delim = QPushButton("/", self)
        self.first_nums = QPlainTextEdit(self)
        self.cheque = QPlainTextEdit(self)

        self.string = ""
        self.first_nums_string = ""
        self.initUI()  # here will be all settings about our design

    def initUI(self):
        self.setGeometry(550, 200, 600, 500)
        self.setWindowTitle("Прятки для виджетов")
        sp = [7, 8, 9, 4, 5, 6, 1, 2, 3]
        self.string = ""
        self.first_nums_string = ""
        self.cheque.resize(600, 20)
        self.cheque.move(0, 0)

        self.first_nums.resize(600, 50)
        self.first_nums.move(0, 20)

        x, y = 175, 70

        for i in range(1, 10):
            btn = QPushButton(str(sp[i - 1]), self)
            btn.resize(70, 70)
            btn.move(x, y)
            btn.clicked.connect(self.add_all)
            btn.clicked.connect(self.fr_num)
            if i % 3 == 0:
                x = 175
                y += 70
            else:
                x += 70

        self.delim.resize(70, 70)
        self.delim.move(385, 70)
        self.delim.clicked.connect(self.add_all)
        self.delim.clicked.connect(self.fr_num)

        self.umnosh = QPushButton("*", self)
        self.umnosh.resize(70, 70)
        self.umnosh.move(385, 140)
        self.umnosh.clicked.connect(self.add_all)
        self.umnosh.clicked.connect(self.fr_num)

        self.minus.resize(70, 70)
        self.minus.move(385, 210)
        self.minus.clicked.connect(self.add_all)
        self.minus.clicked.connect(self.fr_num)

        self.plus.resize(70, 70)
        self.plus.move(385, 280)
        self.plus.clicked.connect(self.add_all)
        self.plus.clicked.connect(self.fr_num)

        self.C.resize(70, 70)
        self.C.move(175, 280)
        self.C.clicked.connect(self.c)

        self.zero.resize(70, 70)
        self.zero.move(245, 280)
        self.zero.clicked.connect(self.add_all)
        self.zero.clicked.connect(self.fr_num)

        self.CE.resize(70, 70)
        self.CE.move(315, 280)
        self.CE.clicked.connect(self.ce)

        self.point.resize(70, 70)
        self.point.move(175, 350)
        self.point.clicked.connect(self.add_all)
        self.point.clicked.connect(self.fr_num)

        self.eq.resize(140, 70)
        self.eq.move(315, 350)
        self.eq.clicked.connect(self.result)

    def add_all(self):
        self.string += self.sender().text()
        self.cheque.setPlainText(self.string)
        print(self.string)

    def fr_num(self):

        if self.sender().text() in "+-*/":
            self.first_nums_string = ""
        else:
            self.first_nums_string += self.sender().text()

        self.first_nums.setPlainText(self.first_nums_string)

    def result(self):
        try:
            res = eval(self.string)
            if '.' in self.string:
                self.string = str(float(res))
                self.cheque.setPlainText(self.string)
                self.first_nums_string = str(float(res))
                self.first_nums.setPlainText(self.first_nums_string)
            else:
                self.string = str(int(res))
                self.cheque.setPlainText(self.string)
                self.first_nums_string = str(int(res))
                self.first_nums.setPlainText(self.first_nums_string)

        except Exception:
            self.first_nums.setPlainText("Error")

    def ce(self):
        self.cheque.setPlainText("")
        self.first_nums.setPlainText("")
        self.string = ""
        self.first_nums_string = ""

    def c(self):
        self.first_nums.setPlainText("")
        self.first_nums_string = ""


if __name__ == '__main__':
    # Создадим класс приложения PyQT
    app = QApplication(sys.argv)
    # А теперь создадим и покажем пользователю экземпляр
    # нашего виджета класса Example
    ex = Example()
    ex.show()
    # Будем ждать, пока пользователь не завершил исполнение QApplication,
    # а потом завершим и нашу программу
    sys.exit(app.exec())
