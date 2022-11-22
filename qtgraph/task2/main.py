from PyQt5 import QtCore, QtMultimedia, uic
from PyQt5.QtCore import Qt
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow, QPushButton
from os.path import join


class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi(join("qtgraph", "task2", "prog.ui"), self)
        self.DO.clicked.connect(self.playMusicBtn)
        self.re.clicked.connect(self.playMusicBtn)
        self.mi.clicked.connect(self.playMusicBtn)
        self.fa.clicked.connect(self.playMusicBtn)
        self.sol.clicked.connect(self.playMusicBtn)
        self.lya.clicked.connect(self.playMusicBtn)
        self.si.clicked.connect(self.playMusicBtn)

    def load_mp3(self, filename):
        media = QtCore.QUrl.fromLocalFile(filename)
        content = QtMultimedia.QMediaContent(media)
        self.player = QtMultimedia.QMediaPlayer()
        self.player.setMedia(content)
    
    def playMusicBtn(self):
        name = self.sender().text().lower()
        path = join("qtgraph", "task2", "notes", f"{name}.mp3")
        self.load_mp3(path)
        self.player.play()
    
    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Q:
            self.DO.click()
        elif event.key() == Qt.Key_W:
            self.re.click()
        elif event.key() == Qt.Key_E:
            self.mi.click()
        elif event.key() == Qt.Key_R:
            self.fa.click()
        elif event.key() == Qt.Key_T:
            self.sol.click()
        elif event.key() == Qt.Key_Y:
            self.lya.click()
        elif event.key() == Qt.Key_U:
            self.si.click()
            # code
        


app = QApplication(sys.argv)
ex = MyWidget()
ex.show()
sys.exit(app.exec_())
