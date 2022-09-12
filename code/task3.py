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
        self.setWindowTitle("Миникалькулятор")

        self.label_fr = QLabel(self)
        self.label_fr.setText("Первое число(целое)")
        self.label_fr.setFont(QFont("Arial", 14))
        self.label_fr.resize(230, 60)
        self.label_fr.move(10, 10)
        self.line_edit_fr = QLineEdit(self)
        self.line_edit_fr.resize(170, 60)
        self.line_edit_fr.move(10, 80)

        self.label_sec = QLabel("Второе число (целое)", self)
        self.label_sec.resize(230, 60)
        self.label_sec.setFont(QFont("Arial", 14))
        self.label_sec.move(10, 150)
        self.line_edit_sec = QLineEdit(self)
        self.line_edit_sec.resize(170, 60)
        self.line_edit_sec.move(10, 210)

        self.btn = QPushButton("->", self)
        self.btn.resize(50, 50)
        self.btn.move(250, 120)
        self.btn.clicked.connect(self.count_all)

        self.label_thr = QLabel("Сумма: ", self)
        self.label_thr.resize(170, 60)
        self.label_thr.setFont(QFont("Arial", 14))
        self.label_thr.move(400, 20)

        self.line_edit_thr = QLineEdit(self)
        self.line_edit_thr.resize(200, 50)
        self.line_edit_thr.move(560, 20)

        self.label_four = QLabel("Разность: ", self)
        self.label_four.resize(170, 60)
        self.label_four.setFont(QFont("Arial", 14))
        self.label_four.move(400, 90)

        self.line_edit_four = QLineEdit(self)
        self.line_edit_four.resize(200, 50)
        self.line_edit_four.move(560, 90)

        self.label_five = QLabel("Произведение: ", self)
        self.label_five.resize(170, 60)
        self.label_five.setFont(QFont("Arial", 14))
        self.label_five.move(400, 160)

        self.line_edit_five = QLineEdit(self)
        self.line_edit_five.resize(200, 50)
        self.line_edit_five.move(560, 160)

        self.label_six = QLabel("Частное: ", self)
        self.label_six.resize(170, 60)
        self.label_six.setFont(QFont("Arial", 14))
        self.label_six.move(400, 230)

        self.line_edit_six = QLineEdit(self)
        self.line_edit_six.resize(200, 50)
        self.line_edit_six.move(560, 230)

    def count_all(self):
        a = self.line_edit_fr.text()
        b = self.line_edit_sec.text()
        if a[0] == '0' and len(a) > 1 or b[0] == '0' and len(b) > 1:
            self.line_edit_six.setText(
                "Error"
            )
            self.line_edit_thr.setText(
                "Error"
            )
            self.line_edit_four.setText(
                "Error"
            )
            self.line_edit_five.setText(
                "Error"
            )
            return
        try:
            a = int(a)
            b = int(b)
        except Exception:
            self.line_edit_six.setText(
                "Error"
            )
            self.line_edit_thr.setText(
                "Error"
            )
            self.line_edit_four.setText(
                "Error"
            )
            self.line_edit_five.setText(
                "Error"
            )
            return

        if b == 0:
            self.line_edit_six.setText(
                "Error"
            )
            self.line_edit_thr.setText(
                str(a + b)
            )
            self.line_edit_four.setText(
                str(a - b)
            )
            self.line_edit_five.setText(
                str(a * b)
            )
        else:
            self.line_edit_thr.setText(
                str(a + b)
            )
            self.line_edit_four.setText(
                str(a - b)
            )
            self.line_edit_six.setText(
                str(a / b)
            )
            self.line_edit_five.setText(
                str(a * b)
            )


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
