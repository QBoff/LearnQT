import sys

from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton
import random

class MyWidget(QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        uic.loadUi("prog.ui", self)
        self.button.setMouseTracking(True)
        self.width = 181
        self.height = 41
        # self.button.clicked.connect(self.moveButton)
        # self.setMouseTracking(True)

    def moveButton(self):
        try:
                
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
        except ValueError:
            print("Your window is too small for me!!!!!!!!!")

    def mouseMoveEvent(self, event):
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
