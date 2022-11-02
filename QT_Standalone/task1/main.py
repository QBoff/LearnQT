import sys

from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt
from PIL import Image, ImageDraw
from random import randrange


class MyWidget(QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        uic.loadUi("QT_Standalone/task1/prog.ui", self)
        self.setMouseTracking(True)
    
    def mousePressEvent(self, event) -> None:
        self.x, self.y = event.x(), event.y()
        
        if event.button() == Qt.LeftButton:
            self.drawCircle()
        elif event.button() == Qt.RightButton:
            self.drawRect()
        self.update()
    
    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Space:
            # self.mousePressEvent()
            self.drawPolygon()
    
    def mouseMoveEvent(self, event) -> None:
        self.x = event.x()
        self.y = event.y()
    
    def drawCircle(self):
        x = QMainWindow.width(self)
        y = QMainWindow.height(self)
        
        p = min(self.x, self.y)
        p2 = min(x, y)
        side = randrange(20, 150)
        
        r, g, b = randrange(0, 255), randrange(0, 255), randrange(0, 255)
        
        im = Image.new("RGB", (x + 30, y + 30), (255, 255, 255))
        draw = ImageDraw.Draw(im)
        
        draw.ellipse(
            (self.x - side // 2, self.y - side // 2, (self.x + side), (self.y + side)), 
            fill=(r, g, b), 
            outline="black"
        )
        im.save("im.png")
        pixmap = QPixmap("im.png")
        height = self.label.contentsRect().height()
        pixmap = pixmap.scaledToHeight(height, Qt.SmoothTransformation)
        self.label.setPixmap(pixmap)
    
    def drawRect(self):
        x = QMainWindow.width(self)
        y = QMainWindow.height(self)
        
        side_x = randrange(1, 160)
        side_y = randrange(1, 160)
        side = min(side_x, side_y)
        r, g, b = randrange(0, 255), randrange(0, 255), randrange(0, 255)
        im = Image.new("RGB", (x - 20, y -20), (255, 255, 255))
        draw = ImageDraw.Draw(im)
        draw.rectangle((self.x - side // 2, self.y - side // 2, self.x + side, self.y + side), 
                     fill=(r, g, b), 
                     outline="black")
        im.save("im.png")
        pixmap = QPixmap("im.png")
        height = self.label.contentsRect().height()
        pixmap = pixmap.scaledToHeight(height, Qt.SmoothTransformation)
        self.label.setPixmap(pixmap)
    
    def drawPolygon(self):
        x = QMainWindow.width(self)
        y = QMainWindow.height(self)
        
        side = randrange(self.x, x)
        h = randrange(self.y, y)
        
        r, g, b = randrange(0, 255), randrange(0, 255), randrange(0, 255)
        im = Image.new("RGB", (x - 20, y -20), (255, 255, 255))
        draw = ImageDraw.Draw(im)
        
        draw.polygon(
            (self.x - side // 2, self.y - h // 2, self.x, self.y + h // 2, self.x + side // 2, self.y - h // 2),
            fill=(r, g, b)
        )
        im.save("im.png")
        
        pixmap = QPixmap("im.png")
        height = self.label.contentsRect().height()
        pixmap = pixmap.scaledToHeight(height, Qt.SmoothTransformation)
        self.label.setPixmap(pixmap)





if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    # print(eval("9!"))
    sys.exit(app.exec_())