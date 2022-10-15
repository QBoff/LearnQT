import sys

from PyQt5 import uic
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PIL import Image, ImageDraw


class Other(Exception):
    pass


class MyWidget(QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        uic.loadUi("PIL_And_Qt_tasks/task2/prog.ui",
                   self)  # место для моего дизайна
        self.counter.setText("3")
        self.show_btn.clicked.connect(self.getData)
        # self.show_btn.clicked.connect(self.drawImage)
    # здесь будут функции для работы с приложением

    def getData(self):
        try:
            self.side_var = float(self.side.text())
            self.coeff_var = float(self.coeff.text())
            self.n_var = float(self.n.text())
            print(self.coeff_var)
            if self.side_var > 406 or self.coeff_var > 1 or self.n_var > 20:
                raise Other
            self.drawImage()
            self.label_2.setText("")
        except ValueError:
            self.error_show.setText("Вы ввели некоректные данные")
            self.show_btn.clicked.connect(self.p)
            count = int(self.counter.text())
            count -= 1
            if count == 0:
                sys.exit()
            else:
                self.counter.setText(str(count))
        except Other:
            self.label_2.setText("Вы превысили мои пределы!!!!!")
            if self.side_var > 406:
                self.label_2.setText("\nВведите side <= 406")
            elif self.coeff_var > 1:
                self.label_2.setText("\nВведите coeff <= 1")
            elif self.n_var > 20:
                self.label_2.setText("\nВведите n <= 20")
            self.show_btn.clicked.connect(self.p)

    def drawImage(self):
        self.side_var = int(self.side_var)
        self.n_var = int(self.n_var)
        im = Image.new("RGB", (self.side_var, self.side_var), (255, 255, 255))
        draw = ImageDraw.Draw(im)
        start_x, start_y = 0, 0
        sv = self.side_var
        for i in range(self.n_var):
            draw.rectangle((start_x, start_y, sv - 1 + start_x, sv - 1 + start_y),
                           fill=(255, 255, 255),
                           outline=(255, 0, 0)
                           )
            start_x += (sv * (1 - self.coeff_var)) // 2
            start_y += (sv * (1 - self.coeff_var)) // 2
            
            sv = int(sv * self.coeff_var)

        im.save("im.png")
        pix = QPixmap("im.png")
        self.image.setPixmap(pix)
    
    def p(self):
        pass


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()

    sys.exit(app.exec_())
