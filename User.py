# -*- coding:utf-8 -*-
import sys
import Database
from PyQt5.QtGui import QIcon, QPainter, QPixmap
from PyQt5.QtWidgets import (QApplication, QWidget, QPushButton,
                             QLabel, QHBoxLayout, QVBoxLayout, QProgressBar)
from PyQt5.QtCore import QTimer, Qt


# UI interface
class UI(QWidget):
    # Setting parameters
    def __init__(self):
        super().__init__()
        self.pos_X = 300
        self.pos_Y = 200
        self.length = 800
        self.height = 600
        self.title = '用户界面'
        self.initUI()  # init UI

    def initUI(self):
        '''Set location, title and icon'''
        # Set the position and size of the window
        # (pos_X, pos_Y, length, height)
        self.setGeometry(self.pos_X, self.pos_Y, self.length, self.height)

        # Set the title of the window
        self.setWindowTitle(self.title)

        # Set window borderless
        # self.setWindowFlags(Qt.FramelessWindowHint)

        # Set the icon of the window (if any)
        self.setWindowIcon(QIcon('./Resources/Icon/Icon1.png'))

        '''Add various controls'''
        # 凑数
        self.label_0 = QLabel('', self)
        # A text box displays prompt information
        self.message_box = QLabel('Message box', self)
        self.message_box.setPixmap(QPixmap('./Resources/Background/Hand.png'))
        # self.message_box.setStyleSheet('background-color: yellow')
        self.box_0 = QProgressBar()  # Replace with label
        self.box_1 = QProgressBar()
        # Four labels show team name
        self.label_A = QLabel('label A', self)
        self.label_B = QLabel('label B', self)
        self.label_C = QLabel('label C', self)
        self.label_D = QLabel('label D', self)
        self.label_A.setPixmap(QPixmap('./Resources/Background/Team_A2.png'))
        self.label_B.setPixmap(QPixmap('./Resources/Background/Team_B2.png'))
        self.label_C.setPixmap(QPixmap('./Resources/Background/Team_C2.png'))
        self.label_D.setPixmap(QPixmap('./Resources/Background/Team_D2.png'))
        # The following four lines fill the label with the background color to observe the size and position
        # self.label_A.setStyleSheet('background-color: yellow')
        # self.label_B.setStyleSheet('background-color: yellow')
        # self.label_C.setStyleSheet('background-color: yellow')
        # self.label_D.setStyleSheet('background-color: yellow')
        # Four progress bar draw balance
        self.box_A = QProgressBar()
        self.box_B = QProgressBar()
        self.box_C = QProgressBar()
        self.box_D = QProgressBar()
        # Three buttons: exit, setting and maximize
        self.button_close = QPushButton('', self)
        # self.button_close.resize(50, 50)
        self.button_close.setStyleSheet('QPushButton{border-image: url(./Resources/Background/Close_1.png)}')
        self.button_close.clicked.connect(self.Re_close)
        self.button_setting = QPushButton('', self)
        # self.button_setting.resize(50, 50)
        self.button_setting.setStyleSheet('QPushButton{border-image: url(./Resources/Background/Setting_1.png)}')
        self.button_setting.clicked.connect(self.Re_setting)
        self.button_full = QPushButton('', self)
        # self.button_full.resize(50, 50)
        self.button_full.setStyleSheet('QPushButton{border-image: url(./Resources/Background/Full_1.png)}')
        self.button_full.clicked.connect(self.Re_full)
        '''Set the box layout'''
        # line 1 - a message box
        self.h_layout_1 = QHBoxLayout()
        self.h_layout_1.addStretch()
        self.h_layout_1.addWidget(self.box_0)  # 测试
        self.h_layout_1.addWidget(self.message_box)
        self.h_layout_1.addWidget(self.box_1)  # 测试
        self.h_layout_1.addStretch()
        # line 2 - team A
        self.h_layout_2 = QHBoxLayout()
        self.h_layout_2.addWidget(self.label_A)
        self.h_layout_2.addWidget(self.box_A)
        # self.h_layout_2.setStretchFactor(self.label_A, 1)
        # self.h_layout_2.setStretchFactor(self.box_A, 3)
        # line 3 - team B
        self.h_layout_3 = QHBoxLayout()
        self.h_layout_3.addWidget(self.label_B)
        self.h_layout_3.addWidget(self.box_B)
        # self.h_layout_3.setStretchFactor(self.label_B, 1)
        # self.h_layout_3.setStretchFactor(self.box_B, 3)
        # line 4 - team C
        self.h_layout_4 = QHBoxLayout()
        self.h_layout_4.addWidget(self.label_C)
        self.h_layout_4.addWidget(self.box_C)
        # self.h_layout_4.setStretchFactor(self.label_C, 1)
        # self.h_layout_4.setStretchFactor(self.box_C, 3)
        # line 5 - team D
        self.h_layout_5 = QHBoxLayout()
        self.h_layout_5.addWidget(self.label_D)
        self.h_layout_5.addWidget(self.box_D)
        # self.h_layout_5.setStretchFactor(self.label_D, 1)
        # self.h_layout_5.setStretchFactor(self.box_D, 3)
        # line 6 - three buttons
        self.h_layout_6 = QHBoxLayout()
        self.h_layout_6.addStretch()
        self.h_layout_6.addWidget(self.button_close)
        self.h_layout_6.addWidget(self.button_setting)
        self.h_layout_6.addWidget(self.button_full)

        # All
        self.v_layout = QVBoxLayout()  # Instantiate a vertical layout manager
        self.v_layout.setContentsMargins(50, 30, 50, 30)  # L U R D
        self.v_layout.setSpacing(20)
        self.v_layout.addLayout(self.h_layout_1)  # message box
        self.v_layout.addLayout(self.h_layout_2)  # team A
        self.v_layout.addLayout(self.h_layout_3)  # team B
        self.v_layout.addLayout(self.h_layout_4)  # team C
        self.v_layout.addLayout(self.h_layout_5)  # team D
        self.v_layout.addLayout(self.h_layout_6)  # buttons
        # self.v_layout.setStretchFactor(self.h_layout_1, 1)
        # self.v_layout.setStretchFactor(self.h_layout_2, 1)
        # self.v_layout.setStretchFactor(self.h_layout_3, 1)
        # self.v_layout.setStretchFactor(self.h_layout_4, 1)
        # self.v_layout.setStretchFactor(self.h_layout_5, 1)
        # self.v_layout.setStretchFactor(self.h_layout_6, 1)

        # 测试
        self.box_A.setValue(10)
        self.box_B.setValue(20)
        self.box_C.setValue(30)
        self.box_D.setValue(40)

        # Set the form layout
        self.setLayout(self.v_layout)

    def Re_close(self):
        # Close the current window
        self.close()

    def Re_setting(self):
        # Enter the setting interface
        pass

    def Re_full(self):
        # Switch between normal size and full screen display
        if self.isMaximized():
            self.showNormal()
        else:
            self.showMaximized()

    def paintEvent(self, event):
        '''
        Function: paintEvent(self, event)
        Usage: Override method A to draw the window background
        '''
        painter = QPainter(self)
        # Method 1: The background is a solid color
        # painter.setBrush(Qt.green)
        # painter.drawRect(self.rect())

        # Method 2: The background is a picture
        my_background = QPixmap('./Resources/Background/Background.png')
        painter.drawPixmap(self.rect(), my_background)

    def keyPressEvent(self, event):
        print(event.key())


if __name__ == '__main__':
    # QApplication is equivalent to the main function,
    # which is the entry point of the program
    app = QApplication(sys.argv)

    # UI interface instantiation
    my_UI = UI()

    # Show main interface
    my_UI.show()

    # Call the exit exit method of the sys library,
    # the condition is app.exec_() (that is, the entire window is closed)
    sys.exit(app.exec_())
