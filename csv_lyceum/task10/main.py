import sys
import csv

from PyQt5.QtWidgets import QApplication, QWidget, QTableWidgetItem
from PyQt5.QtCore import Qt, QVariant
from PyQt5 import uic


class Window(QWidget):
    def __init__(self) -> None:
        super().__init__()
        self.initUI()

    def check(self, split, conditions):
        for splitIndex, value in conditions.items():
            if split[splitIndex] != value:
                return False
        return True

    def lt(self, conditions=dict()):
        with open('rez.csv', encoding="utf8") as csvfile:
            reader = csv.reader(csvfile, delimiter=',', quotechar='"')
            title = ['Фамилия', 'Результат']
            next(reader)
            self.table.setColumnCount(len(title))
            self.table.setHorizontalHeaderLabels(title)
            self.table.setRowCount(0)
            for i, row in enumerate(reader):
                user_name = row[1].split()
                if self.check(user_name, conditions):
                    self.table.setRowCount(
                        self.table.rowCount() + 1)

                    surname = user_name[3]
                    score = row[-1]
                    print(surname, score)

                    item1 = QTableWidgetItem()
                    item1.setData(Qt.EditRole, QVariant(surname))

                    item2 = QTableWidgetItem()
                    item2.setData(Qt.EditRole, QVariant(int(score)))

                    self.table.setItem(i, 0, item1)
                    self.table.setItem(i, 1, item2)
            self.table.resizeColumnsToContents()

    def initUI(self):

        uic.loadUi('csv_lyceum/task10/prog.ui', self)

        self.submitButton.clicked.connect(self.onClick)
        self.schoolInput.addItem('Все')
        self.classInput.addItem('Все')

        schools = set()
        classes = set()
        with open('rez.csv', encoding="utf-8") as file:
            reader = csv.DictReader(file, delimiter=',')
            for row in reader:
                school, classs = row['user_name'].split()[1:3]
                schools.add(school)
                classes.add(classs)

        self.schoolInput.addItems(sorted(schools, key=int))
        self.classInput.addItems(sorted(classes, key=int))
        self.lt()

    def onClick(self):
        school = self.schoolInput.currentText()
        classs = self.classInput.currentText()
        conditions = dict()

        if school != 'Все':
            conditions[1] = school
        if classs != 'Все':
            conditions[2] = classs

        self.lt(conditions)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec_())
