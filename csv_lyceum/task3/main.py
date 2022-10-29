import sys
import csv

from PyQt5.QtWidgets import QApplication, QWidget, QTableWidgetItem
from PyQt5.QtCore import Qt, QVariant
from PyQt5 import uic

# разобрать как это можно сделать самому
class ChequeWindow(QWidget):
    def __init__(self) -> None:
        super().__init__()
        self.initUI()
        self.prices = dict.fromkeys(range(self.table.rowCount()), 0)

    def initUI(self) -> None:
        uic.loadUi('csv_lyceum/task3/prog.ui', self)

        with open('price.csv', encoding="utf8") as csvfile:
            reader = csv.reader(csvfile, delimiter=';')
            title = next(reader) + ['Количество']
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
        self.adjustSize()
        self.setFixedSize(self.size())

    def onCountChange(self, row, column):
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