from instr import *
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QLabel, QApplication, QHBoxLayout, QVBoxLayout, QPushButton, QWidget


class Final_Win(QWidget):
    def __init__(self, exp):
        super().__init__()
        self.initUI()
        self.set_appear()
        self.show()
        self.exp = exp

    def initUI(self):
        self.result_text = QLabel(result_text_ + self.result()) 
        self.index_text = QLabel(index_text_ + self.index)
        self.line1 = QVBoxLayout()
        self.line1.addWidget(self.index_text, alignment=Qt.AlignCenter)
        self.line1.addWidget(self.result_text, alignment=Qt.AlignCenter)

        self.setLayout(self.line1)


    def set_appear(self):
        self.setWindowTitle(final_window)
        self.resize(win_width, win_heights)
        self.move(win_x, win_y)

    def results(self):
        self.index = str(((t1 + t2 + t3)*4 - 200)/10)
        if self.exp.age >= 15:
            if self.index >= 15:
                return txt_res1

            elif self.index >= 11 and self.index <= 15:
                return txt_res2

            elif self.index >= 6 and self.index <= 11:
                return txt_res3

            elif self.index >= 0.5 and self.index <= 6:
                return txt_res4

            elif self.index <= 0.5:
                return txt_res5

        if self.exp.age >= 13 and self.exp.age <= 14:
            if self.index >= 16.5:
                return txt_res1

            elif self.index >= 12.5 and self.index <= 16.5:
                return txt_res2

            elif self.index >= 7.5 and self.index <= 12.5:
                return txt_res3

            elif self.index >= 2 and self.index <= 7.5:
                return txt_res4

            elif self.index <= 2:
                return txt_res5

        if self.exp.age >= 11 and self.exp.age <= 12:
            if self.index >= 18:
                return txt_res1

            elif self.index >= 14 and self.index <= 18:
                return txt_res2

            elif self.index >= 9 and self.index <= 14:
                return txt_res3

            elif self.index >= 3.5 and self.index <= 9:
                return txt_res4

            elif self.index <= 3.5:
                return txt_res5

        if self.exp.age >= 9 and self.exp.age <= 10:
            if self.index >= 19.5:
                return txt_res1

            elif self.index >= 15.5 and self.index <= 19.5:
                return txt_res2

            elif self.index >= 10.5 and self.index <= 15.5:
                return txt_res3

            elif self.index >= 5 and self.index <= 10.5:
                return txt_res4

            elif self.index <= 9:
                return txt_res5

        if self.exp.age >= 7 and self.exp.age <= 8:
            if self.index >= 21:
                return txt_res1

            elif self.index >= 17 and self.index <= 21:
                return txt_res2

            elif self.index >= 12 and self.index <= 17:
                return txt_res3

            elif self.index >= 6.5 and self.index <= 12:
                return txt_res4

            elif self.index <= 6.5:
                return txt_res5

        if self.exp.age < 7:
            return 'нет данных для этого возраста'







        