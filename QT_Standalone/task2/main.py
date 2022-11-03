import sys

from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QTextEdit, QHBoxLayout
from PyQt5.QtGui import QPixmap, QPainter, QImage, QPen
from PyQt5.QtCore import Qt, QPoint, QSize
from PIL import Image, ImageDraw
from random import choice, randrange as rd
from itertools import groupby


class MyWidget(QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        uic.loadUi("QT_Standalone/task2/prog.ui", self)
        self.image = QPixmap("dp.png")
        self.im = Image.open("dp.png")
        self.drawing = False
        self.lastPoint = QPoint()

    def paintEvent(self, event):
        if self.drawing:
            painter = QPainter(self)
            im_x, im_y = self.im.size
            x, y = max(0, self.lastPoint.x()), max(0, self.lastPoint.y())
            x, y = min(x, QMainWindow.width(
                self) - im_x), min(y, QMainWindow.height(self) - im_y)
            painter.drawPixmap(QPoint(x, y), self.image)

    def reDraw(self):
        pov = []
        svc = ()
        colors = self.im.getcolors()
        tr = []
        for i, j in groupby(colors, key=lambda x: x[-1]):
            tr.append(list(j))
        tr = sorted(tr, key=lambda x: x[0], reverse=True)
        color = choice(tr[:6])
        # print(color[0][-1])
        to_color = [(128, 0, 128), (255, 0, 255), (205, 92, 92),
                    (250, 128, 114), (205, 92, 92), (250, 128, 114)]
        color_to = choice(to_color)

        im = self.im.convert("RGB")
        x, y = im.size
        pixels = im.load()

        for i in range(x):
            for j in range(y):
                # pixels[i, j]
                if pixels[i, j] == color[0][-1]:
                    pixels[i, j] = color_to
            
        im.save("dp.png")
        self.image = QPixmap("dp.png")

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Space:
            self.reDraw()

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.drawing = True
            self.lastPoint = event.pos()

    def mouseMoveEvent(self, event):
        if event.buttons() and Qt.LeftButton and self.drawing:
            self.lastPoint = event.pos()

            self.update()

    def mouseReleaseEvent(self, event):
        if event.button == Qt.LeftButton:
            self.drawing = False

    def sizeHint(self):
        return self.image.size()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    # print(eval("9!"))
    sys.exit(app.exec_())
