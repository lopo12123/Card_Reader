# -*- coding:utf-8 -*-
import sys
import Database
from PyQt5.QtGui import QIcon, QPainter, QPixmap
from PyQt5.QtWidgets import (QApplication, QWidget, QPushButton, QLabel,
                             QLineEdit, QHBoxLayout, QVBoxLayout, QProgressBar,
                             QComboBox, QGraphicsOpacityEffect)
from PyQt5.QtCore import QTimer, Qt

# Some global variables
User_number_g = 0  # Total number of users / default 0
User_id_g = [0] * 16  # Create a new array of size 16 to store user id


class Image:
    '''
    Create a class to store image resources
    '''
    Icon1 = './Resources/Icon/Icon1.png'  # Icons
    Icon2 = './Resources/Icon/Icon2.png'
    Background = './Resources/Background/Background.png'  # Background
    Success = './Resources/Background/Success.png'  # Success
    Fail = './Resources/Background/Fail.png'  # Fail
    Team_A = './Resources/Background/Team_A.png'  # Team A / B / C / D
    Team_B = './Resources/Background/Team_B.png'
    Team_C = './Resources/Background/Team_C.png'
    Team_D = './Resources/Background/Team_D.png'
    Unknown = './Resources/Background/Unknown.png'  # symbol '?'
    Hand = './Resources/Background/Hand.png'  # symbol 'hand'


# UI guide1: Know how many users
class UI_guide1(QWidget):
    # Setting parameters
    def __init__(self):
        super().__init__()
        self.pos_X = 475
        self.pos_Y = 340
        self.length = 300
        self.height = 350
        self.title = 'Guide'
        self.user_number = None  # 4 - 16
        self.initUI()  # init UI

    # Initialize the UI interface
    def initUI(self):
        '''Set location, title and icon'''
        self.setGeometry(self.pos_X, self.pos_Y, self.length, self.height)

        # Set the title of the window
        self.setWindowTitle(self.title)

        # Set the icon of the window (if any)
        self.setWindowIcon(QIcon(Image.Icon2))

        # Set window borderless
        # self.setWindowFlags(Qt.FramelessWindowHint)

        # title image
        self.title_text = QLabel(self)
        self.title_text.setPixmap(
            QPixmap('./Resources/Background/Setting_2.png'))
        self.title_text.resize(50, 50)
        self.title_text.move(125, 20)

        # numebr text
        self.number_text = QLabel('<h2>请选择用户数量:</h2>', self)
        self.number_text.setAlignment(Qt.AlignCenter)
        self.number_text.resize(200, 40)
        self.number_text.move(50, 100)

        # number box
        self.number_box = QComboBox(self)
        self.number_box.resize(100, 30)
        self.number_box.move(100, 160)
        self.number_box.addItems([
            '<请选择>', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13',
            '14', '15', '16'
        ])

        # cancel button
        self.cancel_button = QPushButton('', self)
        self.cancel_button.resize(100, 50)
        self.cancel_button.move(40, 250)
        self.cancel_button.setStyleSheet(
            'QPushButton{border-image: url(./Resources/Background/Cancel.png)}'
        )
        self.cancel_button.clicked.connect(self.Re_cancel)

        # check button
        self.check_button = QPushButton('', self)
        self.check_button.resize(100, 50)
        self.check_button.move(160, 250)
        self.check_button.setStyleSheet(
            'QPushButton{border-image: url(./Resources/Background/Check.png)}'
        )
        self.check_button.clicked.connect(self.Re_check)

    def Re_cancel(self):
        # Close the current window
        self.close()

    def Re_check(self):
        global User_number_g, User_id_g
        # check all
        result = self.number_box.currentText()
        if result != '<请选择>':
            self.user_number = int(result)
            User_number_g = self.user_number
            User_id_g = [0] * 16
            self.close()
            my_Guide2.show()

    def paintEvent(self, event):
        '''
        Function: paintEvent(self, event)
        Usage: Override method 'paintEvent' to draw the window background
        '''
        painter = QPainter(self)
        # Method 1: The background is a solid color
        # painter.setBrush(Qt.green)
        # painter.drawRect(self.rect())

        # Method 2: The background is a picture
        my_background = QPixmap(Image.Background)
        painter.drawPixmap(self.rect(), my_background)


# UI guide2: Know their numbers
class UI_guide2(QWidget):
    # Setting parameters
    def __init__(self):
        super().__init__()
        self.pos_X = 475
        self.pos_Y = 340
        self.length = 300
        self.height = 350
        self.title = 'Guide'
        self.now_number = 1  # now_number <= (global)User_number_g
        self.initUI()  # init UI

    # Initialize the UI interface
    def initUI(self):
        '''Set location, title and icon'''
        self.setGeometry(self.pos_X, self.pos_Y, self.length, self.height)

        # Set the title of the window
        self.setWindowTitle(self.title)

        # Set the icon of the window (if any)
        self.setWindowIcon(QIcon(Image.Icon2))

        # Set window borderless
        # self.setWindowFlags(Qt.FramelessWindowHint)

        # title image
        self.title_text = QLabel(self)
        self.title_text.setPixmap(
            QPixmap('./Resources/Background/Setting_2.png'))
        self.title_text.resize(50, 50)
        self.title_text.move(125, 20)

        # numebr text
        self.number_text = QLabel('<h2>请输入第' + str(self.now_number) + '个用户:</h2>', self)
        self.number_text.setAlignment(Qt.AlignCenter)
        self.number_text.resize(200, 40)
        self.number_text.move(50, 100)

        # number box
        self.number_box = QLineEdit(self)
        self.number_box.resize(150, 40)
        self.number_box.move(75, 170)

        # next button
        self.next_button = QPushButton('下一个', self)
        self.next_button.resize(100, 50)
        self.next_button.move(160, 250)
        # self.check_button.setStyleSheet('QPushButton{border-image: url(./Resources/Background/Check.png)}')
        self.next_button.clicked.connect(self.Re_next)

    def Re_next(self):
        global User_number_g, User_id_g, flag

        max_user = User_number_g  # the max of self.now_number
        User_id_g[self.now_number - 1] = int(self.number_box.text())  # Store id

        self.number_box.clear()  # clear
        self.number_box.setFocus()  # wait for next insert

        if self.now_number < max_user:
            self.now_number += 1  # count ++
            self.number_text.setText('<h2>请输入第' + str(self.now_number) + '个用户:</h2>')  # change the title
            if self.now_number == max_user:
                self.next_button.setText('确认')
        elif self.now_number == max_user:  # end insert
            # print(User_id_g)
            self.close()
            # Draw the main UI interface according to the input
            self.Draw_UI()
            my_UI.show()

    def Draw_UI(self):
        global User_number_g, User_id_g
        line_number = User_number_g  # how many lines need to be added

        my_UI.New_line(line_number)

        # print(User_number_g)
        # print(User_id_g)

    def paintEvent(self, event):
        '''
        Function: paintEvent(self, event)
        Usage: Override method 'paintEvent' to draw the window background
        '''
        painter = QPainter(self)
        # Method 1: The background is a solid color
        # painter.setBrush(Qt.green)
        # painter.drawRect(self.rect())

        # Method 2: The background is a picture
        my_background = QPixmap(Image.Background)
        painter.drawPixmap(self.rect(), my_background)


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

        # about team set
        self.team_insert = False  # Are you currently entering a team
        self.team_now = 0
        self.team_set = False  # undo

        self.team_A_id = None  # 删
        self.team_B_id = None
        self.team_C_id = None
        self.team_D_id = None

        # about operate
        self.step = -1
        self.player1_id = None
        self.symbol = 1  # take - '1'; give - '-1'
        self.player2_id = None
        self.number = 0

        # about display
        '''
        h_layout_group(QHBoxLayout)
         * (player: 4/5/6/7/8) A QHBoxLayout layout contains a label and a bar
         * (player: 9/10/11/12/13/14/15/16) A QHBoxLayout layout contains 2 labels and 2 bars
        '''
        self.h_layout_group = []
        self.label_group = []
        self.bar_group = []

        self.my_max = None
        self.my_min = None
        self.my_limit = None
        self.A_value = 0  # default value
        self.B_value = 0
        self.C_value = 0
        self.D_value = 0

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
        self.setWindowIcon(QIcon(Image.Icon1))
        '''Add various controls'''
        self.team_box = QLineEdit(self)
        self.team_box.resize(100, 30)
        self.team_box.move(-120, -50)  # move out of the screen
        self.focus_box = QLabel(self)
        self.focus_box.resize(10, 10)
        self.focus_box.move(-20, -20)  # move out of the screen

        # Four labels display prompt information
        self.message_box_player1 = QLabel('Left box', self)
        self.message_box_player1.setPixmap(QPixmap(Image.Unknown))

        self.message_box_action = QLabel('Middle box', self)
        self.message_box_action.setPixmap(QPixmap(Image.Hand))

        self.message_box_player2 = QLabel('Right box', self)
        self.message_box_player2.setPixmap(QPixmap(Image.Unknown))

        self.message_box_result = QLabel('Result', self)
        self.message_box_result.setPixmap(QPixmap(Image.Success))

        # Four labels show team name
        '''self.label_A = None
        self.label_A = QLabel('label A', self)
        self.label_A.setPixmap(QPixmap(Image.Team_A))

        self.label_B = QLabel('label B', self)
        self.label_B.setPixmap(QPixmap(Image.Team_B))

        self.label_C = QLabel('label C', self)
        self.label_C.setPixmap(QPixmap(Image.Team_C))

        self.label_D = QLabel('label D', self)
        self.label_D.setPixmap(QPixmap(Image.Team_D))'''

        # The following four lines fill the label with the
        # background color to observe the size and position
        # self.label_A].setStyleSheet('background-color: yellow')
        # self.label_B.setStyleSheet('background-color: yellow')
        # self.label_C.setStyleSheet('background-color: yellow')
        # self.label_D.setStyleSheet('background-color: yellow')

        # Four progress bar are used to draw balance
        '''self.box_A = QProgressBar()
        self.box_B = QProgressBar()
        self.box_C = QProgressBar()
        self.box_D = QProgressBar()'''

        # Three buttons: exit, setting and maximize
        self.button_close = QPushButton('', self)
        self.button_close.setMinimumSize(40, 40)
        self.button_close.setStyleSheet(
            'QPushButton{border-image: url(./Resources/Background/Close_1.png)}'
        )
        self.button_close.clicked.connect(self.Re_close)

        self.button_setting = QPushButton('', self)
        self.button_setting.setMinimumSize(40, 40)
        self.button_setting.setStyleSheet(
            'QPushButton{border-image: url(./Resources/Background/Setting_1.png)}'
        )
        self.button_setting.clicked.connect(self.Re_setting)

        self.button_full = QPushButton('', self)
        self.button_full.setMinimumSize(40, 40)
        self.button_full.setStyleSheet(
            'QPushButton{border-image: url(./Resources/Background/Full_1.png)}'
        )
        self.button_full.clicked.connect(self.Re_full)
        '''Set the box layout'''
        # line 1 - a message box
        self.h_layout_head = QHBoxLayout()
        self.h_layout_head.addStretch()
        self.h_layout_head.addWidget(self.message_box_player1)  # player1
        self.h_layout_head.addWidget(self.message_box_action)  # action
        self.h_layout_head.addWidget(self.message_box_player2)  # player2
        self.h_layout_head.addWidget(self.message_box_result)  # result
        self.h_layout_head.addStretch()

        '''# line 2 - team A
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
        # self.h_layout_5.setStretchFactor(self.box_D, 3)'''

        # line 6 - three buttons
        self.h_layout_end = QHBoxLayout()
        self.h_layout_end.addStretch()
        self.h_layout_end.addWidget(self.button_close)
        self.h_layout_end.addWidget(self.button_setting)
        self.h_layout_end.addWidget(self.button_full)

        # Put six horizontal layouts into a vertical layout
        self.v_layout = QVBoxLayout()  # Instantiate a vertical layout manager
        self.v_layout.setContentsMargins(50, 30, 50, 30)  # L U R D
        self.v_layout.setSpacing(20)

        # a message box line
        self.v_layout.addStretch(1)
        self.v_layout.addLayout(self.h_layout_head)  # message box

        # add the team lines
        # All additions are placed in UI_guide2.Draw_UI
        '''self.v_layout.addStretch(2)
        self.v_layout.addLayout(self.h_layout_2)  # team A
        self.v_layout.addStretch(2)
        self.v_layout.addLayout(self.h_layout_3)  # team B
        self.v_layout.addStretch(2)
        self.v_layout.addLayout(self.h_layout_4)  # team C
        self.v_layout.addStretch(2)
        self.v_layout.addLayout(self.h_layout_5)  # team D'''

        ''' The bottom three buttons
        self.v_layout.addStretch(1)
        self.v_layout.addLayout(self.h_layout_end)  # buttons
        self.v_layout.addStretch(0.7) '''

        # self.New_line(8) - # self.New_line(num): num means there are 'num' players

        # Set the form layout
        self.setLayout(self.v_layout)
        self.focus_box.setFocus()

        # self.Set_limit()  # set limits
        # self.Change_value()  # update the progress bar

    def New_line(self, num):
        # 'num' indicates how many players are there
        if num <= 8:  # 4 / 5 / 6 / 7 / 8
            # Every step of the cycle create a new line layout
            for i in range(num):
                team_label = QLabel('', self)  # team label
                team_label.setPixmap(QPixmap(Image.Team_A))
                self.label_group.append(team_label)

                team_bar = QProgressBar()  # team progressbar
                self.bar_group.append(team_bar)

                team_layout = QHBoxLayout()  # H Box layout
                team_layout.addWidget(team_label)
                team_layout.addWidget(team_bar)
                self.h_layout_group.append(team_layout)

            # Add the row layout to the main interface
            for item in self.h_layout_group:
                self.v_layout.addStretch(2)
                self.v_layout.addLayout(item)

            # Finally, add the three buttons below
            self.v_layout.addStretch(1)
            self.v_layout.addLayout(self.h_layout_end)
            self.v_layout.addStretch(0.7)
        
        elif 8 < num <= 16:  # 9-16
            if (num % 2) == 0:  # even
                # Every step of the cycle create a new line layout
                # Each row contains information about two players
                for i in range(int(num / 2)):
                    team_label_1 = QLabel('', self)  # team label
                    team_label_1.setPixmap(QPixmap(Image.Team_A))
                    self.label_group.append(team_label_1)

                    team_label_2 = QLabel('', self)
                    team_label_2.setPixmap(QPixmap(Image.Team_A))
                    self.label_group.append(team_label_2)

                    team_bar_1 = QProgressBar()  # team progressbar
                    self.bar_group.append(team_bar_1)

                    team_bar_2 = QProgressBar()
                    self.bar_group.append(team_bar_2)

                    team_layout = QHBoxLayout()  # H Box layout
                    team_layout.addWidget(team_label_1)
                    team_layout.addWidget(team_bar_1)
                    team_layout.addWidget(team_label_2)
                    team_layout.addWidget(team_bar_2)
                    self.h_layout_group.append(team_layout)
            elif (num % 2) == 1:  # odd
                # Every step of the cycle create a new line layout
                # Each row contains information about two players
                for i in range(int((num + 1) / 2)):
                    # team label
                    team_label_1 = QLabel('', self)
                    team_label_1.setPixmap(QPixmap(Image.Team_A))
                    self.label_group.append(team_label_1)

                    team_label_2 = QLabel('', self)
                    team_label_2.setPixmap(QPixmap(Image.Team_A))
                    self.label_group.append(team_label_2)

                    # team progressbar
                    team_bar_1 = QProgressBar()
                    self.bar_group.append(team_bar_1)

                    team_bar_2 = QProgressBar()
                    self.bar_group.append(team_bar_2)

                    if(i == int((num + 1) / 2) - 1):
                        # Set the transparency to 100% so that
                        # it is not displayed but takes place
                        op1 = QGraphicsOpacityEffect()
                        op1.setOpacity(0)
                        team_label_2.setGraphicsEffect(op1)
                        op2 = QGraphicsOpacityEffect()
                        op2.setOpacity(0)
                        team_bar_2.setGraphicsEffect(op2)

                    # H Box layout
                    team_layout = QHBoxLayout()
                    team_layout.addWidget(team_label_1)
                    team_layout.addWidget(team_bar_1)
                    team_layout.addWidget(team_label_2)
                    team_layout.addWidget(team_bar_2)
                    self.h_layout_group.append(team_layout)

            # Add the row layout to the main interface
            for item in self.h_layout_group:
                self.v_layout.addStretch(2)
                self.v_layout.addLayout(item)

            # Finally, add the three buttons below
            self.v_layout.addStretch(1)
            self.v_layout.addLayout(self.h_layout_end)
            self.v_layout.addStretch(0.7)

    def Set_limit(self):
        # 全改
        # Set maximum, minimum and limit
        Database.Create_DB()  # get data
        result = Database.Get_Setting()
        self.my_max = result[0][1]
        self.my_min = result[0][2]
        self.my_limit = result[0][3]
        Database.Close_database()

        self.box_A.setRange(self.my_min, self.my_max)  # set limit
        self.box_B.setRange(self.my_min, self.my_max)
        self.box_C.setRange(self.my_min, self.my_max)
        self.box_D.setRange(self.my_min, self.my_max)

        self.box_A.setFormat('%v')  # set format
        self.box_B.setFormat('%v')
        self.box_C.setFormat('%v')
        self.box_D.setFormat('%v')

    def Change_value(self):
        # 全改
        # Update the progress bar
        self.box_A.setValue(self.A_value)
        self.box_B.setValue(self.B_value)
        self.box_C.setValue(self.C_value)
        self.box_D.setValue(self.D_value)

    def Re_close(self):
        # Close the current window
        self.close()

    def Re_setting(self):
        # Enter the setting interface
        my_Setting.Get_Settings()
        my_Setting.show()

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
        my_background = QPixmap(Image.Background)
        painter.drawPixmap(self.rect(), my_background)

    def keyPressEvent(self, event):
        '''
        Function: keyPressEvent(self, event)
        Usage: Add response to keyboard events
        Note: F1 - 16777264
              F2 - 16777265
              F3 - 16777266
              F4 - 16777267
              F5 - 16777268
              F6 - 16777269
              '.' - 46
              Enter - 16777220
              Backspace - 16777219 *
        '''
        # team_set is False - unset
        # Start insert the card number and
        # change the focus on which control
        '''
        if self.team_set is False and self.team_insert is False and event.key(
        ) == 46:
            self.team_insert = True
            self.team_box.clear()

        # Inserting and Get which user the input key represents
        if self.team_set is False and self.team_insert is True:
            if event.key() == 16777266:
                self.team_now = 1  # team A
                self.team_box.setFocus()
            elif event.key() == 16777267:
                self.team_now = 2
                self.team_box.setFocus()
            elif event.key() == 16777268:
                self.team_now = 3
                self.team_box.setFocus()
            elif event.key() == 16777269:
                self.team_now = 4
                self.team_box.setFocus()

        # End input and handle events
        if self.team_set is False and self.team_insert is True and event.key(
        ) == 16777220:
            self.team_insert = False
            self.focus_box.setFocus()  # disable lineedit box
            if self.team_now == 1:  # set four team id
                self.team_A_id = int(self.team_box.text())
                self.team_box.clear()
            elif self.team_now == 2:
                self.team_B_id = int(self.team_box.text())
                self.team_box.clear()
            elif self.team_now == 3:
                self.team_C_id = int(self.team_box.text())
                self.team_box.clear()
            elif self.team_now == 4:
                self.team_D_id = int(self.team_box.text())
                self.team_box.clear()
            if self.team_A_id:  # all is set
                if self.team_B_id:
                    if self.team_C_id:
                        if self.team_D_id:
                            self.team_set = True  # all the team is set well
                            self.Set_team()'''

        # team_set is True - set well
        if self.team_set is True:
            if self.step == -1:  # step-1: clear all and wait for insert
                self.team_box.clear()
                self.team_box.setFocus()
                self.step = 0
            if self.step == 0:  # step0: get the player1`s id / know add or sub
                if event.key() == 16777264:  # add
                    self.symbol = 1
                    self.focus_box.setFocus()
                    self.player1_id = int(self.team_box.text())
                    self.team_box.clear()
                    self.step = 1
                elif event.key() == 16777265:  # sub
                    self.symbol = -1
                    self.focus_box.setFocus()
                    self.player1_id = int(self.team_box.text())
                    self.team_box.clear()
                    self.step = 1
            if self.step == 1:  # step1: get the player2`s id
                if event.key() == 16777266:
                    self.player2_id = self.team_A_id
                    self.team_box.setFocus()
                    self.step = 2
                elif event.key() == 16777267:
                    self.player2_id = self.team_B_id
                    self.team_box.setFocus()
                    self.step = 2
                elif event.key() == 16777268:
                    self.player2_id = self.team_C_id
                    self.team_box.setFocus()
                    self.step = 2
                elif event.key() == 16777269:
                    self.player2_id = self.team_D_id
                    self.team_box.setFocus()
                    self.step = 2
            if self.step == 2:  # step2: get the number to add / sub
                if event.key() == 16777220:
                    self.number = int(self.team_box.text())
                    self.team_box.clear()
                    self.focus_box.setFocus()
                    self.Solve()
                    self.step = -1

    def Set_team(self):
        # set the initial value of the four teams
        Database.Create_DB()  # connect
        self.A_value = Database.Select_user(self.team_A_id)[2]  # team A
        self.B_value = Database.Select_user(self.team_B_id)[2]  # team B
        self.C_value = Database.Select_user(self.team_C_id)[2]  # team C
        self.D_value = Database.Select_user(self.team_D_id)[2]  # team D
        Database.Close_database()  # disconnect

        self.Change_value()  # update

    def Solve(self):
        '''
        self.step = -1
        self.player1_id = None
        self.symbol = 1  # take - '1'; give - '-1'
        self.player2_id = None
        self.number = 0
        '''
        p1, p2 = self.sort()

        # print(p1, p2)
        # print('----')

        # Single limit exceeded
        if self.number > self.my_limit:
            self.message_box_result.setPixmap(QPixmap(Image.Fail))
        # Insufficient balance
        elif self.number > self.A_value or self.number > self.B_value or self.number > self.C_value or self.number > self.D_value:
            self.message_box_result.setPixmap(QPixmap(Image.Fail))
        # p1 Take p2
        elif self.symbol == 1:  # p1 <- p2
            self.message_box_result.setPixmap(QPixmap(Image.Success))
            # player 1
            if p1 == 1:  # p1 = team A
                self.A_value += self.number
            elif p1 == 2:  # p1 = team B
                self.B_value += self.number
            elif p1 == 3:  # p1 = team C
                self.C_value += self.number
            elif p1 == 4:  # p1 = team D
                self.D_value += self.number
            # player 2
            if p2 == 1:  # p1 = team A
                self.A_value -= self.number
            elif p2 == 2:  # p1 = team B
                self.B_value -= self.number
            elif p2 == 3:  # p1 = team C
                self.C_value -= self.number
            elif p2 == 4:  # p1 = team D
                self.D_value -= self.number
        # p1 Give p2
        elif self.symbol == -1:  # p1 -> p2
            self.message_box_result.setPixmap(QPixmap(Image.Success))
            # player 1
            if p1 == 1:  # p1 = team A
                self.A_value -= self.number
            elif p1 == 2:  # p1 = team B
                self.B_value -= self.number
            elif p1 == 3:  # p1 = team C
                self.C_value -= self.number
            elif p1 == 4:  # p1 = team D
                self.D_value -= self.number
            # player 2
            if p2 == 1:  # p1 = team A
                self.A_value += self.number
            elif p2 == 2:  # p1 = team B
                self.B_value += self.number
            elif p2 == 3:  # p1 = team C
                self.C_value += self.number
            elif p2 == 4:  # p1 = team D
                self.D_value += self.number

        # Update the progress bar
        self.Change_value()

    def sort(self):
        player1 = None
        player2 = None

        if self.player1_id == self.team_A_id:  # team A
            player1 = 1
            self.message_box_player1.setPixmap(QPixmap(Image.Team_A))
        elif self.player1_id == self.team_B_id:  # team B
            player1 = 2
            self.message_box_player1.setPixmap(QPixmap(Image.Team_B))
        elif self.player1_id == self.team_C_id:  # team C
            player1 = 3
            self.message_box_player1.setPixmap(QPixmap(Image.Team_C))
        elif self.player1_id == self.team_D_id:  # team D
            player1 = 4
            self.message_box_player1.setPixmap(QPixmap(Image.Team_D))

        if self.player2_id == self.team_A_id:  # team A
            player2 = 1
            self.message_box_player2.setPixmap(QPixmap(Image.Team_A))
        elif self.player2_id == self.team_B_id:  # team B
            player2 = 2
            self.message_box_player2.setPixmap(QPixmap(Image.Team_B))
        elif self.player2_id == self.team_C_id:  # team C
            player2 = 3
            self.message_box_player2.setPixmap(QPixmap(Image.Team_C))
        elif self.player2_id == self.team_D_id:  # team D
            player2 = 4
            self.message_box_player2.setPixmap(QPixmap(Image.Team_D))

        return player1, player2


class UI_setting(QWidget):
    # Setting parameters
    def __init__(self):
        super().__init__()
        self.pos_X = 475
        self.pos_Y = 340
        self.length = 300
        self.height = 350
        self.title = 'Setting'
        self.my_max = None  # Set the maximum and minimum balance
        self.my_min = None
        self.my_limit = None  # Set a single deduction limit
        self.initUI()  # init UI

    # Initialize the UI interface
    def initUI(self):
        '''Set location, title and icon'''
        self.setGeometry(self.pos_X, self.pos_Y, self.length, self.height)

        # Set the title of the window
        self.setWindowTitle(self.title)

        # Set the icon of the window (if any)
        self.setWindowIcon(QIcon(Image.Icon2))

        # Set window borderless
        # self.setWindowFlags(Qt.FramelessWindowHint)

        # label - Setting
        self.title_text = QLabel(self)
        self.title_text.setPixmap(
            QPixmap('./Resources/Background/Setting_2.png'))
        self.title_text.resize(50, 50)
        self.title_text.move(125, 10)

        # Set the maximum balance
        self.max_text = QLabel('<h2>MAX</h2>', self)
        self.max_text.resize(40, 50)
        self.max_text.move(75, 80)

        self.max_box = QLineEdit(self)
        self.max_box.resize(100, 30)
        self.max_box.move(125, 90)

        # Set the minimum balance
        self.min_text = QLabel('<h2>MIN</h2>', self)
        self.min_text.resize(40, 50)
        self.min_text.move(75, 150)

        self.min_box = QLineEdit(self)
        self.min_box.resize(100, 30)
        self.min_box.move(125, 160)

        # Set a single deduction limit
        self.limit_text = QLabel('<h2>LIMIT</h2>', self)
        self.limit_text.resize(65, 50)
        self.limit_text.move(50, 220)

        self.limit_box = QLineEdit(self)
        self.limit_box.resize(100, 30)
        self.limit_box.move(125, 230)

        # Get the current setting value and display
        self.Get_Settings()

        # Two buttons
        self.cancel_button = QPushButton('', self)
        self.cancel_button.resize(100, 50)
        self.cancel_button.move(40, 280)
        self.cancel_button.setStyleSheet(
            'QPushButton{border-image: url(./Resources/Background/Cancel.png)}'
        )
        self.cancel_button.clicked.connect(self.Re_cancel)

        self.check_button = QPushButton('', self)
        self.check_button.resize(100, 50)
        self.check_button.move(160, 280)
        self.check_button.setStyleSheet(
            'QPushButton{border-image: url(./Resources/Background/Check.png)}')
        self.check_button.clicked.connect(self.Re_check)

    def Get_Settings(self):
        # Get the current setting value and display
        Database.Create_DB()  # connect

        result = Database.Get_Setting()
        self.max_box.setText(str(result[0][1]))
        self.min_box.setText(str(result[0][2]))
        self.limit_box.setText(str(result[0][3]))

        Database.Close_database()  # disconnect

    def Re_cancel(self):
        # Close the current window
        self.close()

    def Re_check(self):
        # Confirm all changes and Set new setting value
        new_max = int(self.max_box.text())
        new_min = int(self.min_box.text())
        new_limit = int(self.limit_box.text())

        Database.Create_DB()  # connect
        Database.New_Setting(new_max, new_min, new_limit)
        Database.Close_database()  # disconnect

        my_UI.Set_limit()

        self.close()

    def paintEvent(self, event):
        '''
        Function: paintEvent(self, event)
        Usage: Override method 'paintEvent' to draw the window background
        '''
        painter = QPainter(self)
        # Method 1: The background is a solid color
        # painter.setBrush(Qt.green)
        # painter.drawRect(self.rect())

        # Method 2: The background is a picture
        my_background = QPixmap(Image.Background)
        painter.drawPixmap(self.rect(), my_background)


if __name__ == '__main__':
    # QApplication is equivalent to the main function,
    # which is the entry point of the program
    app = QApplication(sys.argv)

    # UI - Guide
    my_Guide1 = UI_guide1()
    my_Guide2 = UI_guide2()

    # UI interface instantiation
    my_UI = UI()

    # UI - Setting
    my_Setting = UI_setting()

    # Show main interface
    my_Guide1.show()

    # Call the exit exit method of the sys library,
    # the condition is app.exec_() (that is, the entire window is closed)
    sys.exit(app.exec_())
