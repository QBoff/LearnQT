import sys
import traceback

from PyQt5 import QtWidgets
from PyQt5.QtWidgets import *

# Унаследуем наш класс от простейшего графического примитива QWidget


def excepthook(exc_type, exc_value, exc_tb):
    tb = "".join(traceback.format_exception(exc_type, exc_value, exc_tb))
    print("error catched!:")
    print("error message:\n", tb)
    QtWidgets.QApplication.quit()
    # or QtWidgets.QApplication.exit(0)


sys.excepthook = excepthook


class Example(QWidget):
    def __init__(self):
        # Надо не забыть вызвать инициализатор базового класса
        super().__init__()
        # В метод initUI() будем выносить всю настройку интерфейса,
        # чтобы не перегружать инициализатор
        self.list_names = ["Чизбургер", "Гамбургер", "Кока-кола", "Нагетсы"]
        self.cheque = QPlainTextEdit(self)
        self.order = QPushButton("Заказать", self)
        # self.check_box1 = QCheckBox("Чизбургер", self)
        # self.line_edit1 = QLineEdit("0", self)
        # self.check_box2 = QCheckBox("Гамбургер", self)
        # self.line_edit2 = QLineEdit("0", self)
        # self.check_box3 = QCheckBox("Кока-кола", self)
        # self.line_edit3 = QLineEdit("0", self)
        # self.check_box4 = QCheckBox("Нагетсы", self)
        # self.line_edit4 = QLineEdit("0", self)
        self.checkboxes = []
        self.initUI()

    def initUI(self):
        # Зададим размер и положение нашего виджета,
        self.setGeometry(550, 200, 600, 300)
        self.setWindowTitle("Прятки для виджетов")

        self.move_checkbox()

        self.order.resize(150, 50)
        self.order.move(20, 135)
        self.order.clicked.connect(self.tocheque)

        self.cheque.resize(320, 200)
        self.cheque.move(230, 10)
        self.cheque.setEnabled(False)

    def tocheque(self):
        orders = "Ваш заказ: \n\n"
        total = 0
        for item in self.checkboxes:
            if item[0].isChecked():
                orders += f"{item[0].text()}----{item[1].text()}---{int(item[2]) * int(item[1].text())}\n"
                total += int(item[2]) * int(item[1].text())

        orders += f"\nИтого: {total}!!!\nНе ешьте много!"
        self.cheque.setPlainText(
            orders
        )


    def isCh(self):
        if self.sender().isChecked():
            for e in self.checkboxes:
                if self.sender() == e[0]:
                    e[1].setText("1")
                    e[1].setEnabled(True)
    
    def move_checkbox(self) -> None:
        x, x2, y = 20, 130, 5
        for i in range(4):
            self.check_box = QCheckBox(self.list_names[i], self)
            self.check_box.move(x, y)
            
            self.line_edit1 = QLineEdit("0", self)
            self.line_edit1.resize(40, 20)
            self.line_edit1.move(x2, y)
            self.line_edit1.setEnabled(False)
            self.check_box.stateChanged.connect(self.isCh)
            self.checkboxes.append([self.check_box, self.line_edit1, 10])
            
            y += 20

if __name__ == '__main__':
    # Создадим класс приложения PyQT
    app = QApplication(sys.argv)
    # А теперь создадим и покажем пользователю экземпляр
    # нашего виджета класса Example
    app.setStyle("fusion")
    app.setStyleSheet("""
                      QCheckBox {
                        spacing: 7px;
                        font-size: 15px;     
                    }
                     QCheckBox::indicator {
                        width: 40px
                        height: 40px
                    }
                      """)
    ex = Example()
    ex.show()
    # Будем ждать, пока пользователь не завершил исполнение QApplication,
    # а потом завершим и нашу программу
    sys.exit(app.exec())
