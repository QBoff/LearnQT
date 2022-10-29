import sys
import csv

from PyQt5.QtWidgets import QApplication, QWidget, QTableWidgetItem
from PyQt5.QtGui import QColor
from PyQt5.QtCore import Qt, QVariant
from PyQt5 import uic
import random as r


class ChequeWindow(QWidget):
    def __init__(self) -> None:
        super().__init__()
        self.initUI()
        self.prices = dict.fromkeys(range(self.table.rowCount()), 0)
        self.canDo = False
        self.refresh.clicked.connect(self.newColor)
        self.table.cellChanged.connect(self.onCountChange)

    def initUI(self) -> None:
        uic.loadUi('csv_lyceum/task4/prog.ui', self)

        with open('price.csv', encoding="utf-8") as file:

            reader = list(csv.reader(file, delimiter=';'))
            title = reader.pop(0) + ['Количество']

            self.table.setColumnCount(len(title))
            self.table.setHorizontalHeaderLabels(title)
            self.table.setRowCount(0)

            for ind1, row in enumerate(reader):
                self.table.setRowCount(self.table.rowCount() + 1)
                for ind2, elem in enumerate(row + ['0']):
                    item = QTableWidgetItem()
                    item.setData(Qt.EditRole, QVariant(
                        int(elem) if elem.isdigit() else elem
                    ))

                    if ind2 in (0, 1):
                        item.setFlags(Qt.ItemIsEnabled)
                    
                    self.table.setItem(ind1, ind2, item)

        self.table.cellChanged.connect(self.onCountChange)
        self.table.cellChanged.connect(self.sortItems)
        self.adjustSize()
        self.setFixedSize(self.size())
    
    
    def sortItems(self):
        self.table.setSortingEnabled(True)
        self.table.sortItems(1, Qt.DescendingOrder)

    def makeNewColors(self):
        return QColor(r.randrange(0, 255), r.randrange(0, 255), r.randrange(0, 255))

    def colorWholeRow(self, index, color):
        for i in range(self.table.columnCount()):
            self.table.item(index, i).setBackground(color)

    def newColor(self):
        self.canDo = True
        colors = [self.makeNewColors() for _ in range(5)]
        for row, col in enumerate(colors):
            self.colorWholeRow(row, col)

        self.canDo = False

    def onCountChange(self, row, column):

        if self.canDo:
            return

        price = int(self.table.item(row, 1).text())
        count = int(self.table.item(row, column).text())

        if count < 0:
            self.table.item(row, column).setText('0')
        else:
            priceNow = price * count
            self.prices[row] = priceNow
            self.result.setText(str(sum(self.prices.values())))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = ChequeWindow()
    window.show()
    sys.exit(app.exec_())
