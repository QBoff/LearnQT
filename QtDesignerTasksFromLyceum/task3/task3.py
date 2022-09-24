import sys

from PyQt5 import uic, QtCore, QtWidgets, QtGui
from PyQt5.QtWidgets import QApplication, QMainWindow


class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("QtDesignerTasksFromLyceum/task3/prog.ui", self)
        self.tasks = []
        self.res_string = ""
        self.result = ""
        # self.add_task.clicked.connect(self.sm)
        self.add_task.clicked.connect(self.get_time)
        self.add_task.clicked.connect(self.btn_get_date)
        self.add_task.clicked.connect(self.push_task)
        self.calendarWidget.clicked.connect(self.get_date)

    @QtCore.pyqtSlot(QtCore.QDate)
    def get_date(self, date):  # <--- date parameter
        self.year = date.year()
        self.month = date.month()
        self.day = date.day()
        
        # print(date.year(), date.month(), date.day())
        # self.res_string += f"{date.year()}-{date.month()}-{date.day()}"
        # self.add_task.clicked.connect(get_date)
    
    def btn_get_date(self):
        self.res_string = ""
        self.res_string += f"{self.year}-{self.month}-{self.day}"
        # print(self.res_string)
    
    def get_time(self):
        self.time_now = self.time.text()
        if len(self.time_now) == 3:
            self.time_now = "00:0" + self.time.now
        elif len(self.time_now) > 3:
            self.time_now = "00:" + self.time_now
        # print(self.time_now)

    def push_task(self):
        self.result = ""
        self.result += self.res_string + " " + self.time_now + " - " + self.string_task.text()
        self.tasks.append(self.result)
        model = QtGui.QStandardItemModel()
        self.listView.setModel(model)
        for i in self.tasks:
            model.appendRow(QtGui.QStandardItem(i))
        print(self.result)
        # self.listView.addItems(self.result)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    # print(eval("9!"))
    sys.exit(app.exec_())
