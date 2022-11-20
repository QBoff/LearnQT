import sys

from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton
import random

class Button(QPushButton):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
    
    def enterEvent(self, event) -> None:
        pass

class MyWidget(QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.setMouseTracking(True)
        uic.loadUi("prog.ui", self)
        self.width = 181
        self.height = 41
        # self.button.clicked.connect(self.moveButton)
        # self.setMouseTracking(True)

    def moveButton(self):
        newX = random.randrange(
            0, QMainWindow.width(self) - self.button.width() - 10)
        newY = random.randrange(
            0, QMainWindow.height(self) - self.button.height() - 10)
        
        while newX in range(self.button.x(), self.button.x() + self.button.width()) and \
                newY in range(self.button.y(), self.button.y() + self.button.height()):
            newX = random.randrange(
                0, QMainWindow.width(self) - self.button.width() - 10)
            newY = random.randrange(
                0, QMainWindow.height(self) - self.button.height() - 10)

        self.button.move(newX, newY)
        # print(newX, newY)
    def getMaximumSide(self):
        windowWidth = QMainWindow.width(self)
        windowHeight = QMainWindow.height(self)
        x, y = self.button.x(), self.button.y()

    def mouseMoveEvent(self, event):
        # print(event.x())
        if event.x() in range(self.button.x(), self.button.x() + self.button.width()) \
            and event.y() in range(self.button.y(), self.button.y() + self.button.height()):
            
            self.moveButton()
            self.update()

    def enterEvent(self, event) -> None:
        if event.x() in range(self.button.x(), self.button.x() + self.button.width()) \
            and event.y() in range(self.button.y(), self.button.y() + self.button.height()):
            
            self.moveButton()
            self.update()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    # print(eval("9!"))
    sys.exit(app.exec_())
