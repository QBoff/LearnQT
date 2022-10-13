import sys

from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog
from PyQt5.QtGui import QPixmap
from PIL import Image


class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("PIL_And_Qt_tasks/task1/prog.ui", self)

        self.angle_anti = 90
        self.angle = -90
        self.last_change = ""

        self.getImage()
        count = 0
        while len(self.image_path) == 0:
            if count > 3:
                sys.exit()

            self.label.setText("Error, укажит енормальный путь в картинке!!!")
            self.getImage()
            count += 1

        # self.im = Image.open(self.image_path)
        self.pixmap = QPixmap(self.image_path).scaled(382, 256)
        self.label.setPixmap(self.pixmap)

        self.make_colors = {
            "R": lambda color: (color[0], 0, 0),
            "G": lambda color: (0, color[1], 0),
            "B": lambda color: (0, 0, color[2]),
            "ALL": lambda color: (color[0], color[1], color[2])
        }

        self.r_btn.clicked.connect(self.onClick)
        self.g_btn.clicked.connect(self.onClick)
        self.b_btn.clicked.connect(self.onClick)
        self.all_btn.clicked.connect(self.onClick)
        self.rotate_anticlockwise.clicked.connect(self.rotate_fun)
        self.rotate_clockwise.clicked.connect(self.rotate_fun)

    def getImage(self):

        self.image_path = QFileDialog.getOpenFileName(
            self, "Выберите картинку", "", "Картинка (*.jpg);;Картинка (*.png);;Все файлы (*)")[0]

    def onClick(self, last_change=""):
        im1 = Image.open(self.image_path)

        im2 = im1.copy()
        pixels = im2.load()
        x, y = im2.size

        for i in range(x):
            for j in range(y):
                pixels[i, j] = self.make_colors[self.sender().text()
                                                ](pixels[i, j])
        self.last_change = self.sender().text()

        save_path = f"{self.image_path.split('/')[-1].split('.')[0]}{self.sender().text()} \
.{self.image_path.split('/')[-1].split('.')[-1]}"

        im2.save(save_path)
        self.pixmap = QPixmap(save_path).scaled(382, 256)
        self.label.setPixmap(self.pixmap)

    def rotate_fun(self):
        im1 = Image.open(self.image_path)

        im2 = im1.copy()
        pixels = im2.load()
        x, y = im2.size

        for i in range(x):
            for j in range(y):
                pixels[i, j] = self.make_colors[self.last_change](pixels[i, j])
                
        if "против" in self.sender().text():
            im2 = im2.rotate(self.angle_anti)
            self.angle_anti += 90
        else:
            im2 = im2.rotate(self.angle)
            self.angle -= 90

        save_path = f"{self.image_path.split('/')[-1].split('.')[0]}{self.sender().text()} \
.{self.image_path.split('/')[-1].split('.')[-1]}"

        im2.save(save_path)
        self.pixmap = QPixmap(save_path).scaled(382, 256)
        self.label.setPixmap(self.pixmap)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    # print(eval("9!"))
    sys.exit(app.exec_())
