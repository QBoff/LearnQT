import sys

from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog
from PyQt5.QtGui import QPixmap
from PIL import Image


class MyWidget(QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        uic.loadUi("PIL_And_Qt_tasks/task3/prog.ui", self)
        self.getImagePath()
        count = 4
        
        while len(self.imagePath) == 0:
            count -= 1
            if count == 0:
                sys.exit()
            
            self.getImagePath()
        pix = QPixmap(self.imagePath)
        self.label.setPixmap(pix)
        self.verticalSlider.setValue(99)
        self.verticalSlider.valueChanged.connect(self.getCurosPoint)
    

    def getCurosPoint(self):
        value = int(self.sender().value())
        im = Image.open(self.imagePath).convert("RGBA")
        im.putalpha(int(2.56 * value))
        im.save("im.png")
        pix = QPixmap("im.png")
        self.label.setPixmap(pix)

    def getImagePath(self):
        self.imagePath = QFileDialog.getOpenFileName(
            self, "Выберите картинку", "", "Картинка (*.jpg);;Картинка (*.png);;Все файлы (*)")[0]


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()

    sys.exit(app.exec_())
