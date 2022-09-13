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

        self.check_box1 = QCheckBox("edit1", self)
        self.label1 = QLabel("edit1", self)
        self.line_edit1 = QLineEdit("edit1", self)
        self.check_box1.resize(20, 20)
        self.check_box1.move(5, 15)
        self.label1.resize(60, 20)
        self.label1.move(30, 15)
        self.line_edit1.resize(100, 20)
        self.line_edit1.move(100, 15)
        self.check_box1.stateChanged.connect(
            lambda: self.hide_or_show(self.line_edit1)
        )

        self.check_box2 = QCheckBox("edit2", self)
        self.label2 = QLabel("edit2", self)
        self.line_edit2 = QLineEdit("edit2", self)
        self.check_box2.resize(20, 20)
        self.check_box2.move(5, 45)
        self.label2.resize(60, 20)
        self.label2.move(30, 45)
        self.line_edit2.resize(100, 20)
        self.line_edit2.move(100, 45)
        self.check_box2.stateChanged.connect(
            lambda: self.hide_or_show(self.line_edit2)
        )

        self.check_box3 = QCheckBox("edit3", self)
        self.label3 = QLabel("edit3", self)
        self.line_edit3 = QLineEdit("edit3", self)
        self.check_box3.resize(20, 20)
        self.check_box3.move(5, 75)
        self.label3.resize(60, 20)
        self.label3.move(30, 75)
        self.line_edit3.resize(100, 20)
        self.line_edit3.move(100, 75)
        self.check_box3.stateChanged.connect(
            lambda: self.hide_or_show(self.line_edit3)
        )

        self.check_box4 = QCheckBox("edit4", self)
        self.label4 = QLabel("edit4", self)
        self.line_edit4 = QLineEdit("edit4", self)
        self.check_box4.resize(20, 20)
        self.check_box4.move(5, 105)
        self.label4.resize(60, 20)
        self.label4.move(30, 105)
        self.line_edit4.resize(100, 20)
        self.line_edit4.move(100, 105)
        self.check_box4.stateChanged.connect(
            lambda: self.hide_or_show(self.line_edit4)
        )

    def hide_or_show(self, ed):
        if ed.isHidden():
            ed.show()
        else:
            ed.hide()


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
