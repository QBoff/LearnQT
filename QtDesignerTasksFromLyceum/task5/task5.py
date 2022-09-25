import sys

from PyQt5 import uic, QtCore, QtWidgets, QtGui
from PyQt5.QtWidgets import *


class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUi()

    def initUi(self):
        self.get_your_matrix()
        self.x = len(self.matrix[0]) * 30 + 300
        self.y = len(self.matrix) * 30 + 300
        self.setGeometry(550, 200, self.x, self.y)
        self.setWindowTitle("Form")
        self.make_matrix()

    # введи матрицу сюда пожалуйста :)
    def get_your_matrix(self):
        self.matrix = [
            [1, 1, 1, 1, 0, 0, 1, 1, 1, 0, 0],
            [0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 1, 0, 0, 0, 0, 0, 1, 1, 1, 1],
        ]

    def make_matrix(self):
        x, y = 10, 10
        for j in range(len(self.matrix)):
            for i in range(len(self.matrix[j])):
                if self.matrix[j][i] == 1:
                    self.btn = QPushButton("*", self)
                    self.btn.resize(30, 30)
                    self.btn.move(x, y)
                    x += 30
                else:
                    self.btn = QPushButton("", self)
                    self.btn.resize(30, 30)
                    self.btn.move(x, y)
                    x += 30
            x = 10
            y += 30


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    # print(eval("9!"))
    sys.exit(app.exec_())
