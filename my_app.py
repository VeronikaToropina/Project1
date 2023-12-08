from instr import *
from PyQt5.QtCore import Qt
from PyQt5.Widgets import QLabel, QApplication, QHBoxLayout, QVBoxLayout, QPushButton, QWidget, QLineEdit
from second_win import Second_Win

class Main_win(QWidgets):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.set_appear()
        self.connects()
        self.show()

    def initUI(self):
        self.text_hello = QLabel(txthello)
        self.text_instruction = QLabel(txtinstruction)
        self.button_start0 = QPushButton(butstart0)
        self.line_fw = QVBoxLayout()
        
        self.line_fw.addWidget(self.text_hello, alignment=AlignLeft)
        self.line_fw.addWidget(self.text_instruction, alignment=AlignLeft)
        self.line_fw.addWidget(self.line_fw, alignment=AlignCenter)

        self.setLayout(self.line_fw)

    def set_appear(self):
        self.setWindowTitle(second_window)
        self.resize(win_width, win_heights)
        self.move(win_x, win_y)

    def next_page(self):
        self.hide()
        self.sw = Second_Win()

    def connects(self):
        self.button_start0.clicked.connect(self.next_page)
        

app = QApplication()
main_win = Main_win()
app.exec_()


