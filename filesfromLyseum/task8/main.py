import sys

from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow


class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("filesfromLyseum/task8/prog.ui", self)
        self.textEdit.setEnabled(False)
        self.load.clicked.connect(self.get_name)
        self.load.clicked.connect(self.load_strings)

    def get_name(self):
        self.name = self.file_name.text()

    def load_strings(self):
        try:
            with open(self.name, "r", encoding="utf-8") as file:
                src = file.read()
                self.textEdit.setText(src)
        except FileNotFoundError:
            pass


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    # print(eval("9!"))
    sys.exit(app.exec_())
