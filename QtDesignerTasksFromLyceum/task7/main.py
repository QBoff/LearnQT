import sys

from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow


class ErrorData(Exception):
    pass


class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("QtDesignerTasksFromLyceum/task7/prog.ui", self)
        self.file_name = ""
        self.data = []
        self.doubleSpinBox.setMaximum(10000000000)
        self.doubleSpinBox.setMinimum(-100000000)
        
        self.doubleSpinBox_2.setMaximum(10000000000)
        self.doubleSpinBox_2.setMinimum(-100000000)
        
        self.doubleSpinBox_3.setMaximum(10000000000)
        self.doubleSpinBox_3.setMinimum(-100000000)
        
        self.btn.clicked.connect(self.get_file_name)
        self.btn.clicked.connect(self.check_the_file)

    def get_file_name(self):
        self.file_name = self.file_nameQT.text()

    def check_the_file(self):
        try:
            with open(self.file_name, "r", encoding="utf-8") as file:
                src = [line.strip().split() for line in file.readlines()]
                new_src = []
                for line in src:
                    for num in line:
                        new_src.append(float(num))
                # src = list(map(lambda x: float(x), [line.strip() for line in file.readlines()]))
                self.doubleSpinBox.setValue(max(new_src))
                self.doubleSpinBox_2.setValue(min(new_src))
                self.doubleSpinBox_3.setValue(sum(new_src) / len(new_src))
                
        except FileNotFoundError:
            self.output_line.setText(f"Файл {self.file_name} не неайден!!!!")
        except ValueError:
            self.output_line.setText(f"В файле {self.file_name} содержаться некоректные данные!!!!!")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    # print(eval("9!"))
    sys.exit(app.exec_())
