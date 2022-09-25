import sys

from PyQt5 import uic, QtCore, QtWidgets, QtGui
from PyQt5.QtWidgets import QApplication, QMainWindow


class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("QtDesignerTasksFromLyceum/task6/prog.ui", self)
        self.result = ""
        self.hod = 1
        self.order.clicked.connect(self.setLCD)
        self.take.clicked.connect(self.logical_Of_AI)
        
    
    def logical_Of_AI(self):
        a = int(self.lcdNumber.value())
        # hod = 1
        # while a != 0:
        if self.hod == -1:
            b = a % 4
            if b == 0:
                b = 2
            if b == 1:
                # print('1', end=' ')
                self.result = 'Компьютер взял - 1'
            else:
                # print(b, end=' ')
                self.result = f"Компьютер взял - {b}"
            self.listWidget.addItem(self.result)
        elif self.hod == 1:
            b = int(self.howShouldTake.text())
            while not (1 <= b <= 3 and b <= a):
                if b < 1 or b > 3:
                    # print('Некорректный ход:', b)
                    self.result = f"Некорректный ход:' {b}"
                    self.listWidget.addItem(self.result)
                    return
                # b = int(self.howShouldTake.text())
            # print(b, end=' ')
            self.result = f"Игрок взял - {b}"
            self.listWidget.addItem(self.result)
        a -= b
        self.hod = -self.hod
        # print(a)
        self.lcdNumber.display(a)
        
        if self.hod == 1 and a == 0:
            # print('ИИ выиграл!')
            self.result = "ИИ выиграл!"
            self.take.setEnabled(False)
            self.listWidget.addItem(self.result)
        elif self.hod == -1 and a == 0:
            # print('Вы выиграли!')
            self.result = "Вы выиграли!"
            self.take.setEnabled(False)
            self.listWidget.addItem(self.result)
    
    def setLCD(self):
        self.lcdNumber.display(self.nom.text())
        

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    # print(eval("9!"))
    sys.exit(app.exec_())
