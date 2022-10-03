import sys

from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow


class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("filesfromLyseum/task9/prog.ui", self)
        self.make_new.clicked.connect(self.get_file_name)
        self.make_new.clicked.connect(self.get_text)
        self.make_new.clicked.connect(self.make_new_file)
        
        self.save_file.clicked.connect(self.get_file_name)
        self.save_file.clicked.connect(self.get_text)
        self.save_file.clicked.connect(self.save_file_as)
        
        self.open_file.clicked.connect(self.get_file_name)
        self.open_file.clicked.connect(self.open_file_as)

    def get_file_name(self):
        self.name = self.file_name.text()
        return self.name

    def get_text(self):
        self.text = self.test_of_file.toPlainText()
        return self.text

    def make_new_file(self):
        try:
            with open(self.get_file_name(), "w", encoding="utf-8") as f:
                f.write(self.get_text())
                
        except FileNotFoundError:
            pass

    def save_file_as(self):
        try:
            with open(self.get_file_name(), "w", encoding="utf-8") as f:
                f.write(self.get_text())
                
        except FileNotFoundError:
            pass

    def open_file_as(self):
        try:
            with open(self.get_file_name(), "r", encoding="utf-8") as f:
                self.test_of_file.setText(f.read())

        except FileNotFoundError:
            pass


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    # print(eval("9!"))
    sys.exit(app.exec_())
