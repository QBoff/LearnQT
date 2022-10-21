import sys


from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5 import uic


class MyWidget(QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        uic.loadUi("QtDesignerTasksFromLyceum/task8/prog.ui", self)
        self.text1 = ""
        self.text2 = ""

        self.compare.clicked.connect(self.get_text)
        self.compare.clicked.connect(self.compare_texts)

    def get_text(self):
        self.text1 = self.code_text_1.toPlainText().split("\n")
        self.text2 = self.code_text_2.toPlainText().split("\n")

        # print(self.text1.split("\n"))

    def compare_texts(self):
        count_equals = 0

        for e in range(len((min(self.text1, self.text2)))):
            if self.text1[e] == self.text2[e]:
                count_equals += 1

        if round(count_equals / len(max(self.text1, self.text2)), 2) * 100 >= float(self.trigger.value()):
            self.result.setStyleSheet("background-color: red")
        else:
            self.result.setStyleSheet("background-color: green")
            
        self.result.setText("Код похож на " +
            str(round(count_equals / len(max(self.text1, self.text2)), 2) * 100) + "%")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    # print(eval("9!"))
    sys.exit(app.exec_())
