import sys
from textwrap import fill

from PyQt5 import uic
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PIL import Image, ImageDraw
import math


class OtherIt(Exception):
    pass


class MyWidget(QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        uic.loadUi("PIL_And_Qt_tasks/task6/prog.ui", self)
        self.count = 3
        self.drawIt.clicked.connect(self.drawOther)

    def drawOther(self):
        try:
            f = float(self.k.text())
            if f >= 1:
                raise OtherIt
            n = int(self.n.text())
            dr = DrawRect(f, n)
            dr.draw_rot_sqr((255, 255))
            dr.im.save("im.png")
            pix = QPixmap("im.png")
            self.image_label.setPixmap(pix)
            
        except ValueError:
            self.count -= 1
            self.error.setText(f"Введите нормальные данные!!!!!! Осталось попыток {self.count}!!")
            if self.count <= 0:
                quit()
        except OtherIt:
            self.count -= 1
            self.error.setText(f"Введите нормальные данные!!!!!! Осталось попыток {self.count}!!")
            if self.count <= 0:
                quit()

class DrawRect:
    def __init__(self, f, n):
        self.im = Image.new('RGB', (510, 510), (255, 255, 255))
        self.draw = ImageDraw.Draw(self.im)
        self.f = f
        self.n = n

    def calc_a(self, L, f):
        return L / 2.0 * (1 - (1 - 2 * (1 - f ** 2)) ** .5)

    def calc_theta(self, L, f, direction='cw'):
        a = self.calc_a(L, f)
        if direction == 'cw':
            d = 1
        elif direction == 'ccw':
            d = -1
        return d*math.asin(a/(f*L))

    def distance(self, ax, ay, bx, by):
        return math.sqrt((by - ay) ** 2 + (bx - ax) ** 2)

    def rotated_about(self, ax, ay, bx, by, angle):
        radius = self.distance(ax, ay, bx, by)
        angle += math.atan2(ay - by, ax - bx)
        return (
            round(bx + radius * math.cos(angle)),
            round(by + radius * math.sin(angle))
        )

    def draw_sqr(self, pos, sqlen, rota):
        square_center = pos
        square_length = sqlen

        square_vertices = (
            (square_center[0] + square_length / 2,
             square_center[1] + square_length / 2),
            (square_center[0] + square_length / 2,
             square_center[1] - square_length / 2),
            (square_center[0] - square_length / 2,
             square_center[1] - square_length / 2),
            (square_center[0] - square_length / 2,
             square_center[1] + square_length / 2)
        )

        square_vertices = [self.rotated_about(x, y, square_center[0], square_center[1], rota) for x, y in
                           square_vertices]
        self.draw.polygon(square_vertices, outline="black")

    def draw_rot_sqr(self, pos):
        side = 500  # starting square side length
        f = self.f     # should be bigger than 1/sqrt(2), for math reasons
        base_theta = self.calc_theta(side, f, direction='cw')
        theta = 0   # first square has no rotation
        for i in range(self.n):
            self.draw_sqr(pos, side, theta)
            # theta is relative to previous square, so we should accumulate it
            theta += base_theta
            side *= f


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()

    sys.exit(app.exec_())
