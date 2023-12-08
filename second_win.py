from instr import *
from PyQt5.QtCore import Qt
from PyQt5.Widgets import QLabel, QApplication, QHBoxLayout, QVBoxLayout, QPushButton, QWidget, QLineEdit
from final_win import Final_Win


class Testswin(QWidgets):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.set_appear()
        self.connects()
        self.show()

    def set_appear():
        self.setWindowTitle(second_window)
        self.resize(win_width, win_heights)
        self.move(win_x, win_y)

    def initUI():
        self.text_fio = QLabel(txtfio)
        self.text_age = QLabel(txtage)
        self.text_result1 = QLabel(txtresult1)
        self.text_start = QLabel(txtstart)
        self.text_result2 = QLabel(txtresult2)
        self.time = QLabel(time)
        self.button_start1 = QPushButton(butstart1)
        self.button_start_prised = QPushButton(butstartprised)
        self.button_start2 = QPushButton(butstart2)
        self.button_send_results = QPushButton(butsendres)
        self.line_fio = QLineEdit(linefio)
        self.line_age = QLineEdit(lineage)
        self.line_puls0 = QLineEdit(linepuls0)
        self.line_puls1 = QLineEdit(linepuls1)
        self.line_puls2 = QLineEdit(linepuls2)

        self.left_line = QVBoxLayout()
        self.right_line = QVBoxLayout()
        self.gorizont_line = QHBoxLayout()

        self.right_line.addWidget(self.time, alignment=Qt.AlignCenter)
        self.left_line.addWidget(self.text_fio, alignment=Qt.AlignLeft)
        self.left_line.addWidget(self.line_fio, alignment=Qt.AlignLeft)
        self.left_line.addWidget(self.text_age, alignment=Qt.AlignLeft)
        self.left_line.addWidget(self.line_age, alignment=Qt.AlignLeft)
        self.left_line.addWidget(self.text_result1, alignment=Qt.AlignLeft)
        self.left_line.addWidget(self.button_start1, alignment=Qt.AlignLeft)
        self.left_line.addWidget(self.line_puls0, alignment=Qt.AlignLeft)
        self.left_line.addWidget(self.text_start, alignment=Qt.AlignLeft)
        self.left_line.addWidget(self.button_start_prised, alignment=Qt.AlignLeft)
        self.left_line.addWidget(self.text_result2, alignment=Qt.AlignLeft)
        self.left_line.addWidget(self.button_start2, alignment=Qt.AlignLeft)
        self.left_line.addWidget(self.line_puls1, alignment=Qt.AlignLeft)
        self.left_line.addWidget(self.line_puls2, alignment=Qt.AlignLeft)
        self.left_line.addWidget(self.button_send_results, alignment=Qt.AlignCenter)
        
        self.gorizont_line.addLayout(self.right_line)
        self.gorizont_line.addLayout(self.left_line)

        self.setLayout(self.gorizont_line)


    def next_page():
        self.hide()
        self.fw = Final_Win()

    def connects():
        self.button_send_results.clicked.connect(self.next_page)
