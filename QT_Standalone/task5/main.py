import sys

from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt
import random

class MyWidget(QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        uic.loadUi("prog.ui", self)
        self.pixmap = QPixmap("ufo.png")
        self.label.setPixmap(self.pixmap)
        # self.button.clicked.connect(self.moveButton)
        # self.setMouseTracking(True)

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_W:
            self.label.move(self.label.x(), (self.label.y() - 5) % QMainWindow.height(self))
        elif event.key() == Qt.Key_D:
            self.label.move((self.label.x() + 5) % QMainWindow.width(self), self.label.y())
        elif event.key() == Qt.Key_A:
            self.label.move((self.label.x() - 5) % QMainWindow.width(self), self.label.y())
        elif event.key() == Qt.Key_S:
            self.label.move(self.label.x(), (self.label.y() + 5) % QMainWindow.height(self))

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    # print(eval("9!"))
    sys.exit(app.exec_())
