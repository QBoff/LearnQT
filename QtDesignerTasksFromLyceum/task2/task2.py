import sys

from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow
from math import pow, sqrt, factorial
import math


class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("QtDesignerTasksFromLyceum/task2/prog.ui", self)
        self.first_color = ""
        self.second_color = ""
        self.third_color = ""
        
        for i in self.buttonGroup.buttons():
            if i.isChecked():
                print(i.text())
        
        self.btn.clicked.connect(self.get_colors)

    def get_colors(self):
        for i in self.buttonGroup.buttons():
            if i.isChecked():
                self.first_color = i.text()
                break
        for j in self.buttonGroup_2.buttons():
            if j.isChecked():
                self.second_color = j.text()
        for ij in self.buttonGroup_3.buttons():
            if j.isChecked():
                self.third_color = ij.text()
        
        self.label_4.setText(
            f"Ваш флаг: {self.first_color}, {self.second_color}, {self.third_color}"
        )


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    # print(eval("9!"))
    sys.exit(app.exec_())
