import sys
import string

# Импортируем из PyQt5.QtWidgets классы для создания приложения и виджета
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *


# Унаследуем наш класс от простейшего графического примитива QWidget
class Example(QWidget):
    def __init__(self):
        # Надо не забыть вызвать инициализатор базового класса
        super().__init__()
        # В метод initUI() будем выносить всю настройку интерфейса,
        # чтобы не перегружать инициализатор
        self.initUI()

    def initUI(self):
        # Зададим размер и положение нашего виджета,
        self.setGeometry(550, 200, 800, 500)
        self.setWindowTitle("Прятки для виджетов")

        self.num1 = QLineEdit(self)
        self.num1.setFont(QFont("Areal", 16))
        self.num1.resize(125, 50)
        self.num1.move(10, 30)

        self.plus = QPushButton('+', self)
        self.plus.resize(70, 50)
        self.plus.move(145, 30)
        self.plus.clicked.connect(lambda: self.count('+'))

        self.minus = QPushButton('-', self)
        self.minus.resize(70, 50)
        self.minus.move(225, 30)
        self.minus.clicked.connect(lambda: self.count('-'))

        self.multip = QPushButton('*', self)
        self.multip.resize(70, 50)
        self.multip.move(305, 30)
        self.multip.clicked.connect(lambda: self.count('*'))

        self.num2 = QLineEdit(self)
        self.num2.setFont(QFont("Areal", 16))
        self.num2.resize(125, 50)
        self.num2.move(385, 30)

        self.lab = QLabel('=', self)
        self.lab.setFont(QFont("Areal", 16))
        self.lab.resize(30, 30)
        self.lab.move(520, 30)

        self.result = QLineEdit(self)
        self.result.setFont(QFont("Areal", 16))
        self.result.resize(125, 50)
        self.result.move(560, 30)

    def count(self, e):
        try:
            num1 = int(self.num1.text())
            num2 = int(self.num2.text())
        except Exception:
            return
        if e == '+':
            self.result.setText(str(num1 + num2))
        elif e == '-':
            self.result.setText(str(num1 - num2))
        elif e == '*':
            self.result.setText(str(num1 * num2))


if __name__ == '__main__':
    # Создадим класс приложения PyQT
    app = QApplication(sys.argv)
    # А теперь создадим и покажем пользователю экземпляр
    # нашего виджета класса Example
    ex = Example()
    ex.show()
    # Будем ждать, пока пользователь не завершил исполнение QApplication,
    # а потом завершим и нашу программу
    sys.exit(app.exec())
