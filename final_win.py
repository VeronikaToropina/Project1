from instr import *
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QLabel, QApplication, QHBoxLayout, QVBoxLayout, QPushButton, QWidget


class Final_Win(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.set_appear()
        self.show()

    def initUI(self):
        self.index_text = QLabel(index_text_)
        self.result_text = QLabel(result_text_)
        self.line1 = QVBoxLayout()
        self.line1.addWidget(self.index_text, alignment=Qt.AlignCenter)
        self.line1.addWidget(self.result_text, alignment=Qt.AlignCenter)

        self.setLayout(self.line1)

    def set_appear(self):
        self.setWindowTitle(final_window)
        self.resize(win_width, win_heights)
        self.move(win_x, win_y)





        