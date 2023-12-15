from instr import *
from PyQt5.QtCore import Qt, QTimer, QTime
from PyQt5.QtWidgets import QLabel, QApplication, QHBoxLayout, QVBoxLayout, QPushButton, QWidget, QLineEdit
from final_win import Final_Win
from PyQt5.QtGui import QFont

class Experiment():
    def __init__(self, age, t1, t2, t3):
        self.age = age
        self.t1 = t1
        self.t2 = t2
        self.t3 = t3


class Testswin(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.set_appear()
        self.connects()
        self.show()

    def set_appear(self):
        self.setWindowTitle(second_window)
        self.resize(win_width, win_heights)
        self.move(win_x, win_y)

    def initUI(self):
        self.text_fio = QLabel(txtfio)
        self.text_age = QLabel(txtage)
        self.text_result1 = QLabel(txtresult1)
        self.text_start = QLabel(txtstart)
        self.text_result2 = QLabel(txtresult2)
        self.text_time = QLabel(txttime)
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

        self.right_line.addWidget(self.text_time, alignment=Qt.AlignCenter)
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


    def next_page(self):
        exp = Experiment(int(self.line_age.text()), int(self.line_puls0.text()), int(self.line_puls1.text()), int(self.line_puls2.text()))

        self.hide()
        self.fw = Final_Win(exp)

    def connects(self):
        self.button_send_results.clicked.connect(self.next_page)
        self.button_start1.clicked.connect(self.timer1)
        self.button_start_prised.clicked.connect(self.timer2)
        self.button_start2.clicked.connect(self.timer3)

    def timer1(self):
        global time
        time = QTime(0, 0, 15)
        self.timer = QTimer()
        self.timer.timeout.connect(self.timer1event)
        self.timer.start(1000)

    def timer1event(self):
        global time
        time = time.addSecs(-1)
        self.text_time.setText(time.toString('hh:mm:ss'))
        self.text_time.setFont(QFont('Times', 36, QFont.Bold))
        self.text_time.setStyleSheet('color: rgb(0, 0, 0)')
        if time.toString('hh:mm:ss') == '00:00:00':
            self.timer.stop()

    def timer2(self):
        global time
        time = QTime(0, 0, 30)
        self.timer = QTimer()
        self.timer.timeout.connect(self.timer2event)
        self.timer.start(1500)

    def timer2event(self):
        global time
        time = time.addSecs(-1)
        self.text_time.setText(time.toString('hh:mm:ss')[6:8])
        self.text_time.setFont(QFont('Times', 36, QFont.Bold))
        self.text_time.setStyleSheet('color: rgb(0, 0, 0)')
        if time.toString('hh:mm:ss') == '00:00:00':
            self.timer.stop()

    def timer3(self):
        global time
        time = QTime(0, 1, 0)
        self.timer = QTimer()
        self.timer.timeout.connect(self.timer3event)
        self.timer.start(1000)

    def timer3event(self):
        global time
        time = time.addSecs(-1)
        self.text_time.setText(time.toString('hh:mm:ss'))
        self.text_time.setFont(QFont('Times', 36, QFont.Bold))
        if int(time.toString('hh:mm:ss')[6:8]) >= 45 or int(time.toString('hh:mm:ss')[6:8]) <= 15:
            self.text_time.setStyleSheet('color: rgb(0, 255, 0)')
        else:
            self.text_time.setStyleSheet('color: rgb(0, 0, 0)')
        if time.toString('hh:mm:ss') == '00:00:00':
            self.timer.stop()




