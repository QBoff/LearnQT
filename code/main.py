
import sys

from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

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

        self.lab = QPushButton("Играть ещё раз", self)

        self.lab.resize(150, 50)
        self.lab.setFont(QFont("Areal", 11))
        self.lab.move(550, 200)
        self.lab.clicked.connect(self.start)

        self.status = QLabel("Статус", self)
        self.status.resize(200, 50)
        self.status.setFont(QFont("Areal", 9))
        self.status.move(550, 260)

        self.switcher = QButtonGroup(self)

        button1 = QRadioButton('X', self)
        button1.resize(50, 50)
        button1.move(200, 10)

        button2 = QRadioButton('0', self)
        button2.resize(50, 50)
        button2.move(260, 10)

        self.switcher.addButton(button1, 0)
        self.switcher.addButton(button2, 1)
        self.switcher.button(0).setChecked(True)

        self.buttons = []
        x = 100
        y = 5

        for i in range(9):

            btn = QPushButton(" ", self)
            self.buttons.append(btn)
            btn.setEnabled(True)
            btn.resize(100, 100)
            btn.clicked.connect(self.process)
            if i % 3 == 0:
                y += 100
                x = 100

            btn.move(x, y)
            x += 100

        print(len(self.buttons))
        print(self.switcher.button(0).text())

    def start(self):
        self.switcher.button(0).setEnabled(True)
        self.switcher.button(1).setEnabled(True)
        self.switcher.button(0).setChecked(True)

        for i in range(9):
            self.buttons[i].setText("")
            self.buttons[i].setEnabled(True)

        self.status.setText(
            self.status.text() + " выберите игрока!"
        )

    def process(self):
        self.status.setText("Играем")

        self.sender().setText(
            self.switcher.button(self.switcher.checkedId()).text()
        )
        self.sender().setEnabled(False)
        self.switcher.button(0).setEnabled(False)
        self.switcher.button(1).setEnabled(False)

        if self.switcher.checkedId() == 0:
            self.switcher.button(1).setChecked(True)
        else:
            self.switcher.button(0).setChecked(True)

        winner = self.winner()
        print(winner)
        if winner != -1:
            self.finish(winner)

        if not self.checkEnabled():
            self.finish(winner)

    def winner(self):
        self.comb = [(0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6),
                     (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6)]

        for position in self.comb:
            if self.buttons[position[0]].text() == self.buttons[position[1]].text() \
                    == self.buttons[position[2]].text() == 'X':
                return 0

            elif self.buttons[position[0]].text() == self.buttons[position[1]].text() \
                    == self.buttons[position[2]].text() == '0':
                return 1

        return -1

    def checkEnabled(self):
        for i in range(9):
            if self.buttons[i].isEnabled():
                return True
        return False

    def finish(self, winner):
        for i in range(9):
            self.buttons[i].setEnabled(False)

        if winner == 0:
            self.status.setText("игрок X выйграл")
        elif winner == 1:
            self.status.setText("игрок 0 выйграл")
        else:
            self.status.setText("ничья")


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
