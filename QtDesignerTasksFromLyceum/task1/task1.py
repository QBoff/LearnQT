import sys

from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow
from math import pow, sqrt, factorial
import math


class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("QtDesignerTasksFromLyceum/calc.ui", self)
        self.string = ""
        self.first_nums_string = ""

        self.table.setDigitCount(15)

        for i in self.buttonGroup_digits.buttons():
            i.clicked.connect(self.add_all)
            # i.clicked.connect(self.fr_num)
        for j in self.buttonGroup_binary.buttons():
            j.clicked.connect(self.add_all)

        self.btn_eq.clicked.connect(self.result)
        self.btn_clear.clicked.connect(self.ce)
        self.btn_sqrt.clicked.connect(self.sqrt)
        self.btn_fact.clicked.connect(self.fac_u)

    def add_all(self):
        if self.sender().text() not in "+-*/^":
            self.string += self.sender().text()
            self.table.display(self.string)
            # print(self.string)
        elif self.sender().text() in "+-*/^":
            if self.sender().text() == '^':
                self.first_nums_string = self.string + "**"
            else:
                self.first_nums_string = self.string + self.sender().text()

            self.string = ""
            self.table.display(self.string)

    # def fr_num(self):

    #     if self.sender().text() in "+-*/":
    #         self.first_nums_string = ""
    #     else:
    #         self.first_nums_string += self.sender().text()

    def result(self):
        try:
            self.string = self.first_nums_string + self.string
            res = eval(self.string)
            if '.' in self.string:
                self.string = str(float(res))
                self.table.display(self.string)
                self.first_nums_string = str(float(res))
            else:
                self.string = str(int(res))
                self.table.display(self.string)
                self.first_nums_string = str(int(res))
        except Exception:
            self.table.display("Error")

    def ce(self):
        self.table.display("")
        self.string = ""
        self.first_nums_string = ""

    def sqrt(self):
        n = float(self.string)
        n = str(sqrt(n))
        self.string = n
        self.table.display(self.string)

    def fac_u(self):
        self.string = str(factorial(int(float(self.string))))
        self.table.display(self.string)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    # print(eval("9!"))
    sys.exit(app.exec_())
