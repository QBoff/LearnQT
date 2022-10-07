import sys

from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtGui import QPixmap
from PIL import Image


class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("PIL_And_Qt_tasks/task1/prog.ui", self)
        
        self.im = Image.open("cat.png")
        self.pixmap = QPixmap("cat.png").scaled(382, 256)
        
        self.make_colors = {
            "R": lambda color: (color[0], 0, 0),
            "G": lambda color: (0, color[1], 0),
            "B": lambda color: (0, 0, color[2])
        }
        
        self.r_btn.clicked.connect(self.onClick)
        self.g_btn.clicked.connect(self.onClick)
        self.b_btn.clicked.connect(self.onClick)
    
    def onClick(self):
        color_of_btn = self.sender().text()
        pixels = self.im.load()
        x, y = self.im.size
        
        for i in range(x):
            for j in range(y):
                pixels[i, j] = self.make_colors[color_of_btn](pixels[i, j])
        
        self.im.save("cat.png")
        self.pixmap = QPixmap("cat.png").scaled(382, 256)
        self.label.setPixmap(self.pixmap)        


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    # print(eval("9!"))
    sys.exit(app.exec_())
