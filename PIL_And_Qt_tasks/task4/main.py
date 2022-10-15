import sys

from PyQt5 import uic
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PIL import Image, ImageDraw
from random import randrange


class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("PIL_And_Qt_tasks/task4/prog.ui", self)

        self.colors_btn.clicked.connect(self.getAmountOfColors)

    def getAmountOfColors(self):
        value, ok_pressed = QInputDialog.getInt(
            self, "Количество цветов", "Какое количество цветов будет?", 1, 1, 9, 1)
        if ok_pressed:

            im = Image.new('RGB', (400, 40 * value), (255, 255, 255))
            draw = ImageDraw.Draw(im)
            length_x = 400
            y = 0
            step = 40

            for i in range(value):
                r, g, b = randrange(0, 255), randrange(
                    0, 255), randrange(0, 255)
                draw.rectangle((0, y, length_x, y + step),
                               fill=(r, g, b), outline=(0, 0, 0))
                y += step

            im.save("im.png")
            pix = QPixmap("im.png")
            self.label.setPixmap(pix)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()

    sys.exit(app.exec_())
