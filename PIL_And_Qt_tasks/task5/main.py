import sys

from PyQt5 import uic
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PIL import Image, ImageDraw
from random import randrange


class MyWidget(QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        uic.loadUi("PIL_And_Qt_tasks/task5/prog.ui", self)

        self.slider.setValue(50)
        self.side = 300
        self.drawStartImage()

        self.slider.valueChanged.connect(self.drawImage)

    def drawImage(self):
        value = int(self.sender().value())
        if value > 50:
            im = Image.new('RGB', (int(self.side * ((49 + value) / 100)),
                           int(self.side * ((49 + value) / 100))), (255, 255, 255))
            side = (int(self.side * ((49 + value) / 100)))
        else:
            im = Image.new('RGB', (int(self.side * ((49 + value) / 100)),
                           int(self.side * ((49 + value) / 100))), (255, 255, 255))
        # im = Image.new('RGB', (self.side * , 300), (255, 255, 255))
            side = (int(self.side * ((49 + value) / 100)))
        draw = ImageDraw.Draw(im)

        draw.ellipse((0, 0, side - 1, side - 1), fill=(
            255, 255, 255), outline=(255, 0, 0))
        draw.ellipse((side // 6, side // 6, side // 3, side // 3), fill=(
            255, 255, 255), outline=(255, 0, 0))
        draw.ellipse((side - side // 3, side // 6, side - side // 3 + side // 6, side // 3), fill=(
            255, 255, 255), outline=(255, 0, 0))
        im.save("im.png")

        pix = QPixmap("im.png")
        self.image_label.setPixmap(pix)

    def drawStartImage(self):
        im = Image.new('RGB', (self.side, self.side), (255, 255, 255))

        draw = ImageDraw.Draw(im)

        draw.ellipse((0, 0, self.side - 1, self.side - 1), fill=(
            255, 255, 255), outline=(255, 0, 0))
        draw.ellipse((self.side // 6, self.side // 6, self.side // 3, self.side // 3), fill=(
            255, 255, 255), outline=(255, 0, 0))
        draw.ellipse((self.side - self.side // 3, self.side // 6,
                      self.side - self.side // 3 + self.side // 6, self.side // 3), fill=(
            255, 255, 255), outline=(255, 0, 0))

        im.save("im.png")
        pix = QPixmap("im.png")
        self.image_label.setPixmap(pix)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()

    sys.exit(app.exec_())
