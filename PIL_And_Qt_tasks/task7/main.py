#!/usr/bin/env python3

# -*- coding: utf-8 -*-

import sys

from PyQt5.QtWidgets import QWidget, QApplication, QPushButton, QMainWindow

from PyQt5.QtWidgets import QInputDialog, QColorDialog

from PyQt5.QtWidgets import QLineEdit, QLabel

from PyQt5.QtGui import QPen, QPainter

from math import pi, cos, sin

from PyQt5.QtCore import Qt


SCREEN_SIZE = [500, 500]


class Example(QMainWindow):

    def __init__(self):

        super().__init__()
        self.flag = False
        # self.button.clicked.connect(self.draf)
        self.initUI()

        # self.draw.clicked.connect(self.draf)

    def initUI(self):

        self.setGeometry(300, 300, *SCREEN_SIZE)

        self.setWindowTitle('Квадрат-объектив')

        self.Lab1 = QLabel(self)

        self.Lab1.move(20, 40)

        self.Lab1.setText("Сторона квадрата")

        self.Lab2 = QLabel(self)

        self.Lab2.move(20, 70)

        self.Lab2.setText("Коэф. Мастабирования")

        self.Lab3 = QLabel(self)

        self.Lab3.move(20, 100)

        self.Lab3.setText("Кол-во повторений")

        self.line = QLineEdit(self)

        self.line.move(70, 40)

        self.line1 = QLineEdit(self)

        self.line1.move(100, 70)

        self.line2 = QLineEdit(self)

        self.line2.move(150, 100)

        self.button = QPushButton(self)

        self.button.move(200, 100)

        self.button.setText("ПУСК")
        
        self.do_paint = False

        self.button.clicked.connect(self.paint)
    
    
    def paint(self):
        self.do_paint = True
        self.repaint()

    def paintEvent(self, event):
        if self.do_paint:
            # Создаем объект QPainter для рисования
            qp = QPainter()
            # Начинаем процесс рисования
            qp.begin(self)
            self.draf(qp)
            # Завершаем рисование
            qp.end()

    def xs(self, x):

        return x + SCREEN_SIZE[0] // 2

    def ys(self, y):

        return SCREEN_SIZE[1] // 2 - y

    def draf(self, qp):

        self.Leng = self.line.text()
        self.Koef = float(self.line1.text())
        self.N = self.line2.text()

        RAD = int(self.Leng)

        p = 6

        # nodes = [(float(RAD * cos(i * 2 * pi / p)), float(RAD * sin(i * 2 * pi / p)))
        #          for i in range(p)]
        nodes = [(float(RAD * sin(i * 2 * pi / p)) * self.Koef, float(RAD * cos(i * 2 * pi / p)) * self.Koef)
                 for i in range(p)]

        nodes2 = [(int(self.xs(node[0])), int(self.ys(node[1]))) for node in nodes]

        for i in range(-1, len(nodes2) - 1):

            qp.drawLine(*nodes2[i], *nodes2[i + 1])

            pen = QPen(Qt.red, 2)

            qp.setPen(pen)

        for i in range(-2, len(nodes2) - 2):

            qp.drawLine(*nodes2[i], *nodes2[i + 2])


if __name__ == '__main__':

    app = QApplication(sys.argv)

    ex = Example()
    ex.show()
    sys.exit(app.exec())
