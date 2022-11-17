import sys
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow
from PyQt5 import uic
 

class MyWidget(QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        uic.loadUi("qtgraph/task1/prog.ui", self)
        self.pushButton.clicked.connect(self.draw)
        
    def draw(self) -> None:
        try:
            if self.lineEdit.text().split() != [] and self.check(self.lineEdit.text()):
                self.graphicsView.clear()
                self.graphicsView.plot([i for i in range(20)], [eval(self.lineEdit.text().split('=')[-1]) for x in range(20)], pen="r")
        except:
            pass
    def check(self, string):
        return string.split('=')[0].strip() == 'y' and 'x' in string.split('=')[1]
 

app = QApplication(sys.argv)
ex = MyWidget()
print("".split())
ex.show()
sys.exit(app.exec_())