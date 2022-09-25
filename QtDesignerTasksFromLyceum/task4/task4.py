import sys

from PyQt5 import uic, QtCore, QtWidgets, QtGui
from PyQt5.QtWidgets import QApplication, QMainWindow


class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("QtDesignerTasksFromLyceum/task4/prog.ui", self)
        self.name = ""
        self.telephone = ""
        self.add_btn.clicked.connect(self.add_to_listWidget)
    
    def get_all_data(self):
        self.name = self.name_input.text()
        self.telephone = self.telephone_input.text()
    
    def add_to_listWidget(self):
        self.get_all_data()
        # я запрещаю вам иметь имя с цифрами и номера с буквами
        if self.telephone.isdigit() and self.name.isalpha():
            self.listWidget.addItem(f"{self.name} {self.telephone}")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    # print(eval("9!"))
    sys.exit(app.exec_())
