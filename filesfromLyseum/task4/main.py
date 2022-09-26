import sys
import random


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
        self.setGeometry(550, 200, 800, 200)
        self.setWindowTitle("Миникалькулятор")

        self.set_btn()
        # print(1)
        self.set_Line_Edit()
        # print(2)
        self.btn.clicked.connect(lambda: self.random_line(
            open("lines.txt", encoding="utf-8")))
        # print(3)

    def set_btn(self):
        self.btn = QPushButton("Получить", self)
        self.btn.resize(170, 70)
        self.btn.move(30, 50)

    def set_Line_Edit(self):
        self.line_edit = QLineEdit(self)
        self.line_edit.resize(570, 70)
        self.line_edit.move(210, 50)

    def random_line(self, afile="lines.txt"):
        line = None
        try:
            line = next(afile)
            for num, aline in enumerate(afile, 2):
                n = random.randrange(num)
                if n:
                    # print(random.randrange(num))
                    continue
                line = aline
            # print(1)
            self.line_edit.setText(line.strip())

        except Exception:
            pass


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
