# -*- coding:utf-8 -*-
import sys
import Database
from PyQt5.QtGui import QIcon, QPainter, QPixmap
from PyQt5.QtWidgets import (QApplication, QWidget, QPushButton, QLabel,
                             QLineEdit, QHBoxLayout, QVBoxLayout, QProgressBar,
                             QComboBox, QGraphicsOpacityEffect, QMessageBox, QListWidget)
from PyQt5.QtCore import QTimer, Qt, QTime, QDate, QDateTime

# Some global variables
User_number_g = 0  # Total number of users / default 0
User_id_g = [0] * 16  # Create a new array of size 16 to store user id
History_number = 1  # the count number of operations, reset when click the reset button


class Image:
    '''
    Create a class to store image resources
    '''
    Icon1 = './Resources/Icon/Icon1.png'  # Icons
    Icon2 = './Resources/Icon/Icon2.png'
    Background = './Resources/Background/Background.png'  # Background
    Success = './Resources/Background/Success.png'  # Success
    Fail = './Resources/Background/Fail.png'  # Fail

    # Team label (1 - 16)
    Team = [] * 16
    Team.append('./Resources/Background/Team1.jpg')  # Team[0]
    Team.append('./Resources/Background/Team2.jpg')
    Team.append('./Resources/Background/Team3.jpg')
    Team.append('./Resources/Background/Team4.jpg')
    Team.append('./Resources/Background/Team5.jpg')
    Team.append('./Resources/Background/Team6.jpg')
    Team.append('./Resources/Background/Team7.jpg')
    Team.append('./Resources/Background/Team8.jpg')
    Team.append('./Resources/Background/Team9.jpg')
    Team.append('./Resources/Background/Team10.jpg')
    Team.append('./Resources/Background/Team11.jpg')
    Team.append('./Resources/Background/Team12.jpg')
    Team.append('./Resources/Background/Team13.jpg')
    Team.append('./Resources/Background/Team14.jpg')
    Team.append('./Resources/Background/Team15.jpg')
    Team.append('./Resources/Background/Team16.jpg')
    Unknown = './Resources/Background/Unknown.png'  # symbol '?'
    Hand = './Resources/Background/Hand.png'  # symbol 'hand'

    # 16 stylesheets
    Style = [] * 16
    Style.append('QProgressBar{text-align: center} QProgressBar::chunk{background: #FF0000;}')  # 0
    Style.append('QProgressBar{text-align: center} QProgressBar::chunk{background: #FFFF00;}')  # 1
    Style.append('QProgressBar{text-align: center} QProgressBar::chunk{background: #80FF00;}')  # 2
    Style.append('QProgressBar{text-align: center} QProgressBar::chunk{background: #00FFFF;}')  # 3
    Style.append('QProgressBar{text-align: center} QProgressBar::chunk{background: #FF80C0;}')  # 4
    Style.append('QProgressBar{text-align: center} QProgressBar::chunk{background: #FF8040;}')  # 5
    Style.append('QProgressBar{text-align: center} QProgressBar::chunk{background: #800000;}')  # 6
    Style.append('QProgressBar{text-align: center} QProgressBar::chunk{background: #808000;}')  # 7
    Style.append('QProgressBar{text-align: center} QProgressBar::chunk{background: #8000FF;}')  # 8
    Style.append('QProgressBar{text-align: center} QProgressBar::chunk{background: #808080;}')  # 9
    Style.append('QProgressBar{text-align: center} QProgressBar::chunk{background: #800080;}')  # 10
    Style.append('QProgressBar{text-align: center} QProgressBar::chunk{background: #FF0080;}')  # 11
    Style.append('QProgressBar{text-align: center} QProgressBar::chunk{background: #C0C0C0;}')  # 12
    Style.append('QProgressBar{text-align: center} QProgressBar::chunk{background: #00FF00;}')  # 13
    Style.append('QProgressBar{text-align: center} QProgressBar::chunk{background: #0000FF;}')  # 14
    Style.append('QProgressBar{text-align: center} QProgressBar::chunk{background: #408080;}')  # 15


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
        self.setWindowFlags(Qt.FramelessWindowHint)

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
            'QPushButton{border-image: url(./Resources/Background/Check.png)}')
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
        self.setWindowFlags(Qt.FramelessWindowHint)

        # title image
        self.title_text = QLabel(self)
        self.title_text.setPixmap(
            QPixmap('./Resources/Background/Setting_2.png'))
        self.title_text.resize(50, 50)
        self.title_text.move(125, 20)

        # numebr text
        self.number_text = QLabel(
            '<h2>请输入第' + str(self.now_number) + '个用户:</h2>', self)
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
        # self.check_button.setStyleSheet('QPushButton{border-image: url(?)}')
        self.next_button.clicked.connect(self.Re_next)

    def Re_next(self):
        global User_number_g, User_id_g, flag

        box_text = self.number_box.text()

        # if: if the box is empty, wait for insert
        if box_text == '':
            self.Warning(2)

        # elif: if the text in the box is not a pure number
        elif (self.is_number(box_text)) is False:
            self.Warning(1)

        # else: if the box get the number, next one
        else:
            max_user = User_number_g  # the max of self.now_number
            User_id_g[self.now_number - 1] = int(box_text)  # Store id

            self.number_box.clear()  # clear
            self.number_box.setFocus()  # wait for next insert

            if self.now_number < max_user:
                self.now_number += 1  # count ++
                self.number_text.setText('<h2>请输入第' + str(self.now_number) +
                                         '个用户:</h2>')  # change the title
                if self.now_number == max_user:
                    self.next_button.setText('确认')
            elif self.now_number == max_user:  # end insert
                # 清空原有记录表, 用于存放当前次操作记录数据
                Database.Create_DB()
                Database.Delete_operate()
                Database.Close_database()
                # print(User_id_g)
                self.close()

                # Draw the main UI interface according to the input
                self.Draw_UI()
                # set the focus on the LineEdit 'team_box' to accept the card id
                my_UI.team_box.setFocus()
                my_UI.step = 0
                my_UI.show()

    def is_number(self, s):
        '''
        Function: is_number(s)
        Usage: Enter a string of characters to determine whether it is a number
        '''
        try:
            int(s)
            return True
        except ValueError:
            return False

    def Warning(self, i):
        if i == 1:
            self.reply = QMessageBox.question(self, '警告！', '请确认帐号为纯数字！', QMessageBox.Yes, QMessageBox.Yes)
        elif i == 2:
            self.reply = QMessageBox.question(self, '警告！', '请输入账号！', QMessageBox.Yes, QMessageBox.Yes)
        self.number_box.setFocus()

    def Draw_UI(self):
        global User_number_g, User_id_g
        line_number = User_number_g  # how many lines need to be added

        my_UI.New_line(line_number)
        my_UI.Set_range()

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
        self.length = 1000
        self.height = 750
        self.title = '用户界面'

        # about operate
        self.step = -1
        self.player_option = -1
        self.player1_id = -1  # player`id cant be -1
        self.player2_id = -1  # if it == -1 -> didn`t get this id
        self.symbol = 0  # take - '1'; give - '-1'
        self.number = -1  # how much money to take

        # about display
        ''' h_layout_group(QHBoxLayout)
         * (player: 4/5/6/7/8)
         A QHBoxLayout layout contains a label and a bar
         * (player: 9/10/11/12/13/14/15/16)
         A QHBoxLayout layout contains 2 labels and 2 bars '''
        self.h_layout_group = []
        self.label_group = []
        self.bar_group = []
        self.value_group = []

        self.my_max = None
        self.my_min = None
        self.my_limit = None

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

        self.team_box = QLineEdit(self)  # a LineEdit to accept the card id
        self.team_box.resize(100, 40)
        self.team_box.move(-120, -50)  # move out of the screen
        self.focus_box = QLabel(self)  # a label to set screen`s focus
        self.focus_box.resize(10, 10)
        self.focus_box.move(-20, -20)  # move out of the screen

        '''Add various controls'''
        # Four labels display prompt information
        self.message_box_player1 = QLabel('Left box', self)
        self.message_box_player1.setPixmap(QPixmap(Image.Unknown))

        self.message_box_action = QLabel('Middle box', self)
        self.message_box_action.setPixmap(QPixmap(Image.Hand))

        self.message_box_player2 = QLabel('Right box', self)
        self.message_box_player2.setPixmap(QPixmap(Image.Unknown))

        self.message_box_number = QLabel('', self)
        self.message_box_number.setMinimumSize(50, 50)
        self.message_box_number.setPixmap(QPixmap(Image.Unknown))

        self.message_box_result = QLabel('Result', self)
        self.message_box_result.setPixmap(QPixmap(Image.Success))

        # Three buttons: exit, setting and maximize
        self.information_box = QLabel('<h3>输入玩家1并选择加减</h3>', self)  # information
        self.information_box.setAlignment(Qt.AlignCenter)
        self.information_box.setMinimumSize(50, 60)

        self.history_list = QListWidget(self)  # history
        self.history_list.setFocusPolicy(Qt.NoFocus)
        self.history_list.setMinimumSize(360, 60)
        self.history_list.setMaximumHeight(90)
        # self.history_list.addItem('日期:' + QDate.currentDate().toString(Qt.ISODate))  # date
        # self.history_list.addItem('时间:' + QTime.currentTime().toString())  # time
        self.history_list.addItem(QDateTime.currentDateTime().toString('yyyy-MM-dd HH:mm:ss') + ' 进入程序')
        
        # the function of button 'close' is replaced by 'save'(name not change)
        # which is used to save all the record of the operatinos
        self.button_close = QPushButton('', self)
        self.button_close.setMinimumSize(40, 40)
        self.button_close.setStyleSheet(
            'QPushButton{border-image: url(./Resources/Background/Save_1.png)}'
        )
        # self.button_close.clicked.connect(self.Re_close)  # changed
        self.button_close.clicked.connect(self.Re_save)

        self.button_setting = QPushButton('', self)
        self.button_setting.setMinimumSize(40, 40)
        self.button_setting.setStyleSheet(
            'QPushButton{border-image: url(./Resources/Background/Setting_1.png)}'
        )
        self.button_setting.clicked.connect(self.Re_setting)

        '''self.button_full = QPushButton('', self)
        self.button_full.setMinimumSize(40, 40)
        self.button_full.setStyleSheet(
            'QPushButton{border-image: url(./Resources/Background/Full_1.png)}'
        )
        self.button_full.clicked.connect(self.Re_full)'''

        self.button_next = QPushButton('', self)
        self.button_next.setMinimumSize(40, 40)
        self.button_next.setStyleSheet(
            'QPushButton{border-image: url(./Resources/Background/Next_1.png)}'
        )
        self.button_next.clicked.connect(self.Re_next)
        '''Set the box layout'''
        # line 1 - a message box
        self.h_layout_head = QHBoxLayout()
        self.h_layout_head.addStretch()
        self.h_layout_head.addWidget(self.message_box_player1)  # player1
        self.h_layout_head.addWidget(self.message_box_action)  # action
        self.h_layout_head.addWidget(self.message_box_player2)  # player2
        self.h_layout_head.addWidget(self.message_box_number)  # number
        self.h_layout_head.addWidget(self.message_box_result)  # result
        self.h_layout_head.addStretch()

        # line 6 - three buttons
        self.h_layout_end = QHBoxLayout()
        self.h_layout_end.addStretch()
        self.h_layout_end.addWidget(self.information_box)
        self.h_layout_end.addStretch()
        self.h_layout_end.addWidget(self.history_list)
        self.h_layout_end.addStretch()
        self.h_layout_end.addWidget(self.button_close)
        self.h_layout_end.addWidget(self.button_setting)
        # self.h_layout_end.addWidget(self.button_full)
        # self.button_full.move(-100, -100)
        self.h_layout_end.addWidget(self.button_next)

        # Put six horizontal layouts into a vertical layout
        self.v_layout = QVBoxLayout()  # Instantiate a vertical layout manager
        self.v_layout.setContentsMargins(50, 30, 50, 30)  # L U R D
        self.v_layout.setSpacing(20)

        # a message box line
        self.v_layout.addStretch(1)
        self.v_layout.addLayout(self.h_layout_head)  # message box

        # add the team lines
        # All additions are placed in UI_guide2.Draw_UI

        # self.New_line(num): num means there are 'num' players

        # Set the form layout
        self.setLayout(self.v_layout)
        self.focus_box.setFocus()

    def set_focus(self):
        self.focus_box.setFocus()

    def New_line(self, num):
        # 'num' indicates how many players are there
        if num <= 8:  # 4 / 5 / 6 / 7 / 8
            # Every step of the cycle create a new line layout
            for i in range(num):
                team_label = QLabel('', self)  # team label
                team_label.setPixmap(QPixmap(Image.Team[i]))
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
                count = 0
                # Every step of the cycle create a new line layout
                # Each row contains information about two players
                for i in range(int(num / 2)):
                    team_label_1 = QLabel('', self)  # team label
                    team_label_1.setPixmap(QPixmap(Image.Team[count]))
                    count += 1
                    self.label_group.append(team_label_1)

                    team_label_2 = QLabel('', self)
                    team_label_2.setPixmap(QPixmap(Image.Team[count]))
                    count += 1
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
                count = 0
                # Every step of the cycle create a new line layout
                # Each row contains information about two players
                for i in range(int((num + 1) / 2)):
                    # team label
                    team_label_1 = QLabel('', self)
                    team_label_1.setPixmap(QPixmap(Image.Team[count]))
                    count += 1
                    self.label_group.append(team_label_1)

                    team_label_2 = QLabel('', self)
                    team_label_2.setPixmap(QPixmap(Image.Team[count]))
                    count += 1
                    self.label_group.append(team_label_2)

                    # team progressbar
                    team_bar_1 = QProgressBar()
                    self.bar_group.append(team_bar_1)

                    team_bar_2 = QProgressBar()
                    self.bar_group.append(team_bar_2)

                    if (i == int((num + 1) / 2) - 1):
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

    def Set_range(self):
        global User_id_g

        # Set maximum, minimum and limit
        Database.Create_DB()  # get max / min / limit
        result = Database.Get_Setting()
        self.my_max = result[0][1]
        self.my_min = result[0][2]
        self.my_limit = result[0][3]
        Database.Close_database()

        # Set Limit(max / min)
        i = 0
        for item in self.bar_group:
            item.setRange(self.my_min, self.my_max)  # set range
            item.setFormat('%v')  # set the display format
            item.setStyleSheet(Image.Style[i])
            i += 1

        # Get Value (in the 'self.value_group')
        self.value_group = []
        Database.Create_DB()
        for item in User_id_g:
            if item != 0:  # the player`s id cant be '0'
                current_value = Database.Select_user(item)
                self.value_group.append(current_value[2])
        Database.Close_database()

        self.Set_value()

    def Set_value(self):
        # Set Valu: Modify the display and modify the contents of the database
        i = 0
        for item in self.value_group:
            self.bar_group[i].setValue(item)  # self.value_group.index(item)
            i += 1

    def Re_close(self):
        # Close the current window
        self.close()

    def Re_save(self):
        # get all the operate record
        Database.Create_DB()
        history_result = Database.Get_operate()
        Database.Close_database()

        fo = open('历史记录.txt', 'w')  # 文件只写, 新操作会覆盖旧文档
        for item in history_result:
            fo.write(item[1])
            fo.write('\n')  # new line
        fo.close()

        self.history_list.addItem('')  # notice the user
        self.history_list.addItem(QDateTime.currentDateTime().toString('yyyy-MM-dd HH:mm:ss') + ' 导出记录成功！')
        self.history_list.scrollToBottom()

        # reset the focus on the 'team_box'
        self.team_box.setFocus()

    def Re_setting(self):
        # Enter the setting interface
        my_Setting.Get_Settings()
        my_Setting.show()

    def Re_full(self):
        # Switch between normal size and full screen display
        if self.isMaximized():
            self.showNormal()
            self.team_box.setFocus()
        else:
            self.showMaximized()
            self.team_box.setFocus()

    def Re_next(self):
        # reset the 'rate' in database
        Database.Create_DB()
        Database.Reset_rate()
        Database.Close_database()

        # Reset the title
        self.message_box_player1.setPixmap(QPixmap(Image.Unknown))
        self.message_box_player2.setPixmap(QPixmap(Image.Unknown))
        self.message_box_number.setPixmap(QPixmap(Image.Unknown))
        self.message_box_result.setPixmap(QPixmap(Image.Success))

        # Reset all the progressbars and their values
        self.Set_range()

        # Reset the step and information
        self.step = 0
        self.change_info(0)

        # Record in history
        self.history_list.addItem('')
        self.history_list.addItem(QDateTime.currentDateTime().toString('yyyy-MM-dd HH:mm:ss') + ' 重置成功！')
        self.history_list.scrollToBottom()

        # Record in database
        global History_number
        my_number = '*OPT' + str(History_number) + ':  '
        my_time = QDateTime.currentDateTime().toString('yyyy-MM-dd HH:mm:ss')
        my_operation = my_time + '  重置数据;'

        Database.Create_DB()
        Database.New_operate(History_number, my_number + my_operation)
        Database.Close_database()

        History_number += 1

        # Set focus
        self.team_box.setFocus()

    def is_number(self, s):
        '''
        Function: is_number(s)
        Usage: Enter a string of characters to determine whether it is a number
        '''
        try:
            int(s)
            return True
        except ValueError:
            return False

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
        Note: key coding:
              F1 - 16777264 - Add(Take)
              F2 - 16777265 - Sub(Give)
              F3 - 16777266 - Double add: multiply the added value by 2
              F4 - 16777267 - Half add: the added value is halved
              F5 - 16777268 - Double sub: multiply the subtracted value by 2
              F6 - 16777269 - Half sub: Decrease by half
              '.' - 46
              L-Enter - 16777220
              R-Enter - 16777221
              Backspace - 16777219
        '''
        global History_number
        # get the text in the 'team_box' then clear the box:
        ''' if it`s valid, use it
        if it`s invalid, ignore it '''
        current_text = self.team_box.text()  # current text
        result = self.is_number(current_text)  # if the text is a number

        self.team_box.clear()

        # Step 2: get the number(how much money to take)
        if self.step == 2 and result is True:
            if event.key() == 16777220 or event.key() == 16777221:  # press 'enter' to confirm
                self.my_move('out')
                self.number = int(current_text)

                self.Solve()
                ''' * Reset all variables for the next read * -- not necessary
                self.player1_id = -1
                self.player2_id = -1
                self.symbol = 0
                self.number = -1 '''
                self.history_list.addItem(QDateTime.currentDateTime().toString('yyyy-MM-dd HH:mm:ss') + ' 确认金额: ' + str(self.number))
                self.history_list.addItem('操作完成')
                self.history_list.scrollToBottom()

                self.step = 0
                result = False
                self.change_info(0)

        # Step 1: get the player2`s id
        if self.step == 1 and result is True:
            # Determine whether the currently entered id belongs to the current player
            if self.right_button(event.key()) is True:
                a = int(current_text)  # 'a' indicates the id of the current input,
                b = False  # 'b' indicates whether there is a current id in the queue
                for item in User_id_g:
                    if item == a:
                        b = True
                        break
                if b is False:
                    # there is no such id in the group 'User_group_g'
                    # print('no such id 2')
                    self.history_list.addItem('')
                    self.history_list.addItem(QDateTime.currentDateTime().toString('yyyy-MM-dd HH:mm:ss') + ' 出错！请输入正确的p2！')
                    self.history_list.scrollToBottom()
                    self.step = 0
                    result = False
                    self.change_info(0)
                else:
                    # Enter the correct id, then record the id of p2
                    if event.key() == 16777220 or event.key() == 16777221:  # press 'enter' to confirm
                        self.player2_id = int(current_text)

                        p2 = chr(ord('A') + User_id_g.index(self.player2_id))
                        if self.symbol == 1:
                            self.history_list.addItem(QDateTime.currentDateTime().toString('yyyy-MM-dd HH:mm:ss') + ' 确认玩家2: ' + p2)
                            self.history_list.scrollToBottom()
                        elif self.symbol == -1:
                            self.history_list.addItem(QDateTime.currentDateTime().toString('yyyy-MM-dd HH:mm:ss') + ' 确认玩家2: ' + p2)
                            self.history_list.scrollToBottom()
                        
                        self.my_move('in')
                        self.step = 2
                        self.change_info(2)

        # Step 0: know symbol`s value
        #         press F1/F2 is also used to check the player1`s id
        if self.step == 0 and result is True:
            # Determine whether the currently entered id belongs to the current player
            if self.right_button(event.key()) is True:
                a = int(current_text)  # 'a' indicates the id of the current input,
                b = False  # 'b' indicates whether there is a current id in the queue
                for item in User_id_g:
                    if item == a:
                        b = True
                        break
                if b is False:
                    # there is no such id in the group 'User_group_g'
                    # print('no such id 1')
                    self.history_list.addItem('')
                    self.history_list.addItem(QDateTime.currentDateTime().toString('yyyy-MM-dd HH:mm:ss') + ' 出错！请输入正确的p1！')
                    self.history_list.scrollToBottom()
                    self.step = 0
                    self.change_info(0)
                else:
                    ''' 1 - now the text in 'team_box' is a number
                        2 - and 'step == 0' means it`s time to choose F1 / F2 '''
                    if event.key() == 16777264:  # key 'F1' - Add
                        self.symbol = 1
                        self.player1_id = int(current_text)

                        p1 = chr(ord('A') + User_id_g.index(self.player1_id))  # get p1`s code(ABCD....)
                        self.history_list.addItem('')
                        self.history_list.addItem(QDateTime.currentDateTime().toString('yyyy-MM-dd HH:mm:ss') + ' 确认玩家1: ' + p1)
                        self.history_list.addItem(QDateTime.currentDateTime().toString('yyyy-MM-dd HH:mm:ss') + ' 确认操作: 加')
                        self.history_list.scrollToBottom()
                        # go to next step
                        self.step = 1
                        self.change_info(1)
                    elif event.key() == 16777265:  # key 'F2' - Sub
                        self.symbol = -1
                        self.player1_id = int(current_text)

                        p1 = chr(ord('A') + User_id_g.index(self.player1_id))  # get p1`s code(ABCD....)
                        self.history_list.addItem('')
                        self.history_list.addItem(QDateTime.currentDateTime().toString('yyyy-MM-dd HH:mm:ss') + ' 确认玩家1: ' + p1)
                        self.history_list.addItem(QDateTime.currentDateTime().toString('yyyy-MM-dd HH:mm:ss') + ' 确认操作: 减')
                        self.history_list.scrollToBottom()
                        # go to next step
                        self.step = 1
                        self.change_info(1)
                    elif event.key() == 16777266:  # key 'F3' - double add
                        # Get id
                        self.player_option = int(current_text)
                        # print(self.player_option)

                        # Change its 'RATE' in sheet 'USER'
                        Database.Create_DB()
                        Database.Update_rate(self.player_option, 2)
                        Database.Close_database()
                        # add record to history
                        p_o = chr(ord('A') + User_id_g.index(self.player_option))  # get p1`s code(ABCD....)
                        self.history_list.addItem('')
                        self.history_list.addItem(QDateTime.currentDateTime().toString('yyyy-MM-dd HH:mm:ss') + ' 设置玩家' + p_o + ': 倍加')
                        self.history_list.scrollToBottom()

                        # Record in database
                        my_number = '*OPT' + str(History_number) + ':  '
                        my_time = QDateTime.currentDateTime().toString('yyyy-MM-dd HH:mm:ss')
                        my_operation = my_time + '  设置玩家' + p_o + ': 倍加;'

                        Database.Create_DB()
                        Database.New_operate(History_number, my_number + my_operation)
                        Database.Close_database()

                        History_number += 1

                        # go to next step
                        self.step = 0
                    elif event.key() == 16777267:  # key 'F4' - half add
                        # Get id
                        self.player_option = int(current_text)
                        # print(self.player_option)

                        # Change its 'RATE' in sheet 'USER'
                        Database.Create_DB()
                        Database.Update_rate(self.player_option, 3)
                        Database.Close_database()
                        # add record to history
                        p_o = chr(ord('A') + User_id_g.index(self.player_option))  # get p1`s code(ABCD....)
                        self.history_list.addItem('')
                        self.history_list.addItem(QDateTime.currentDateTime().toString('yyyy-MM-dd HH:mm:ss') + ' 设置玩家' + p_o + ': 半加')
                        self.history_list.scrollToBottom()

                        # Record in database
                        my_number = '*OPT' + str(History_number) + ':  '
                        my_time = QDateTime.currentDateTime().toString('yyyy-MM-dd HH:mm:ss')
                        my_operation = my_time + '  设置玩家' + p_o + ': 半加;'

                        Database.Create_DB()
                        Database.New_operate(History_number, my_number + my_operation)
                        Database.Close_database()

                        History_number += 1

                        # go to next step
                        self.step = 0
                    elif event.key() == 16777268:  # key 'F5' - double sub
                        # Get id
                        self.player_option = int(current_text)
                        # print(self.player_option)

                        # Change its 'RATE' in sheet 'USER'
                        Database.Create_DB()
                        Database.Update_rate(self.player_option, 4)
                        Database.Close_database()
                        # add record to history
                        p_o = chr(ord('A') + User_id_g.index(self.player_option))  # get p1`s code(ABCD....)
                        self.history_list.addItem('')
                        self.history_list.addItem(QDateTime.currentDateTime().toString('yyyy-MM-dd HH:mm:ss') + ' 设置玩家' + p_o + ': 倍减')
                        self.history_list.scrollToBottom()

                        # Record in database
                        my_number = '*OPT' + str(History_number) + ':  '
                        my_time = QDateTime.currentDateTime().toString('yyyy-MM-dd HH:mm:ss')
                        my_operation = my_time + '  设置玩家' + p_o + ': 倍减;'

                        Database.Create_DB()
                        Database.New_operate(History_number, my_number + my_operation)
                        Database.Close_database()

                        History_number += 1

                        # go to next step
                        self.step = 0
                    elif event.key() == 16777269:  # key 'F6' - half sub
                        # Get id
                        self.player_option = int(current_text)
                        # print(self.player_option)

                        # Change its 'RATE' in sheet 'USER'
                        Database.Create_DB()
                        Database.Update_rate(self.player_option, 5)
                        Database.Close_database()
                        # add record to history
                        p_o = chr(ord('A') + User_id_g.index(self.player_option))  # get p1`s code(ABCD....)
                        self.history_list.addItem('')
                        self.history_list.addItem(QDateTime.currentDateTime().toString('yyyy-MM-dd HH:mm:ss') + ' 设置玩家' + p_o + ': 半减')
                        self.history_list.scrollToBottom()

                        # Record in database
                        my_number = '*OPT' + str(History_number) + ':  '
                        my_time = QDateTime.currentDateTime().toString('yyyy-MM-dd HH:mm:ss')
                        my_operation = my_time + '  设置玩家' + p_o + ': 半减;'

                        Database.Create_DB()
                        Database.New_operate(History_number, my_number + my_operation)
                        Database.Close_database()

                        History_number += 1

                        # go to next step
                        self.step = 0

    def my_move(self, where):
        if where == 'out':
            self.team_box.move(-120, -50)
            # print('move out')
        elif where == 'in':
            self.team_box.setPlaceholderText('请输入金额')
            self.team_box.move(120, 65)
            # print('move in')

    def right_button(self, button_number):
        if 16777264 <= button_number <= 16777269:  # F1 - F6
            return True
        elif button_number == 16777220 or button_number == 16777221:
            return True
        else:
            return False

    def change_info(self, num):
        if num == 0:
            self.information_box.setText('<h3>输入玩家1并选择加减</h3>')
        elif num == 1:
            self.information_box.setText('<h3>输入玩家2并确认</h3>')
        elif num == 2:
            self.information_box.setText('<h2>请输入金额</h2>')
        else:
            pass

    def Solve(self):
        global User_id_g

        # Find out p1 and p2`s index in 'User_id_g[]'
        for item in User_id_g:
            if item == self.player1_id:
                p1_index = User_id_g.index(item)
            if item == self.player2_id:
                p2_index = User_id_g.index(item)

        # Get the balance of current player 1 and player 2
        p1_current_value = self.value_group[p1_index]
        p2_current_value = self.value_group[p2_index]

        # Get the magnification of p1 and p2
        Database.Create_DB()
        p1_rate_get = Database.Select_user(self.player1_id)[3]
        p2_rate_get = Database.Select_user(self.player2_id)[3]
        # print(str(p1_rate_get) + '/' + str(p2_rate_get))
        Database.Close_database()

        if p1_rate_get == 1:
            p1_rate_add = 1
            p1_rate_sub = 1
        elif p1_rate_get == 2:
            p1_rate_add = 2
            p1_rate_sub = 1
        elif p1_rate_get == 3:
            p1_rate_add = 0.5
            p1_rate_sub = 1
        elif p1_rate_get == 4:
            p1_rate_add = 1
            p1_rate_sub = 2
        elif p1_rate_get == 5:
            p1_rate_add = 1
            p1_rate_sub = 0.5

        if p2_rate_get == 1:
            p2_rate_add = 1
            p2_rate_sub = 1
        elif p2_rate_get == 2:
            p2_rate_add = 2
            p2_rate_sub = 1
        elif p2_rate_get == 3:
            p2_rate_add = 0.5
            p2_rate_sub = 1
        elif p2_rate_get == 4:
            p2_rate_add = 1
            p2_rate_sub = 2
        elif p2_rate_get == 5:
            p2_rate_add = 1
            p2_rate_sub = 0.5

        # print(str(p1_rate_add) + '/' + str(p1_rate_sub) + '/' + str(p2_rate_add) + '/' + str(p2_rate_sub))

        # 1 The information prompt area displays Player 1 and Player 2
        self.message_box_player1.setPixmap(QPixmap(Image.Team[p1_index]))  # p1
        self.message_box_player2.setPixmap(QPixmap(Image.Team[p2_index]))  # p2
        self.message_box_number.setText('<h2>' + str(self.number) + '</h2>')  # number
        self.message_box_number.setAlignment(Qt.AlignCenter)

        # 2 Determine whether the operation succeeded or failed
        # (1) Deduction exceeds limit - fail
        should_number = max(p1_rate_sub, p2_rate_sub) * self.number
        if should_number > self.my_limit:
            self.message_box_result.setPixmap(QPixmap(Image.Fail))
        else:
            # (2) Insufficient balance in 2 cases
            # Player 1 takes player 2’s money, but player 2’s money is not enough
            if self.symbol == 1 and p2_current_value < (self.number * p2_rate_sub):
                self.message_box_result.setPixmap(QPixmap(Image.Fail))
            # Player 2 takes player 1’s money, but player 1’s money is not enough
            elif self.symbol == -1 and p1_current_value < (self.number * p1_rate_sub):
                self.message_box_result.setPixmap(QPixmap(Image.Fail))
            else:
                # (3) Successful operation
                self.message_box_result.setPixmap(QPixmap(Image.Success))
                # p1 takes p2`s money(p1+/p2-)
                if self.symbol == 1:
                    p1_current_value += (self.number * p1_rate_add)  # Calculate balance
                    p2_current_value -= (self.number * p2_rate_sub)
                    opt = ' 加 '
                # p2 takes p1`s money(p1-/p2+)
                elif self.symbol == -1:
                    p1_current_value -= (self.number * p1_rate_sub)  # Calculate balance
                    p2_current_value += (self.number * p2_rate_add)
                    opt = ' 减 '

                # double/half add/sub only takes effect once
                Database.Create_DB()
                Database.Update_rate(self.player1_id, 1)
                Database.Update_rate(self.player2_id, 1)
                Database.Close_database()

                self.value_group[p1_index] = p1_current_value  # Update balance
                self.value_group[p2_index] = p2_current_value

                # * save the operation in the database
                '''Database.Create_DB()
                Database.Update_one(self.player1_id, p1_current_value)
                Database.Update_one(self.player2_id, p2_current_value)
                Database.Close_database()'''
                p1_name = chr(ord('A') + self.player1_id - 1)
                p2_name = chr(ord('A') + self.player2_id - 1)

                '''
                print('p1 name:' + p1_name + ';' + 'p2 name:' + p2_name)
                print('金额:' + str(self.number))
                print('p1:' + str(p1_current_value) + '  p2:' + str(p2_current_value))
                '''
                # the operate record
                global History_number
                my_number = '*OPT' + str(History_number) + ':  '
                my_time = QDateTime.currentDateTime().toString('yyyy-MM-dd HH:mm:ss')
                my_operation = '  P1: ' + p1_name + ', P2: ' + p2_name + ', 金额: ' + str(self.number) + '; 操作: ' + p1_name + opt + p2_name + ' ' + str(self.number) + ';'
                # print(my_number + my_time + my_operation)

                Database.Create_DB()
                Database.New_operate(History_number, my_number + my_time + my_operation)
                Database.Close_database()

                History_number += 1

                self.Set_value()


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
        self.setWindowFlags(Qt.FramelessWindowHint)

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
        my_UI.team_box.setFocus()

        self.close()

    def Re_check(self):
        # Confirm all changes and Set new setting value
        new_max = int(self.max_box.text())
        new_min = int(self.min_box.text())
        new_limit = int(self.limit_box.text())

        Database.Create_DB()  # connect
        Database.New_Setting(new_max, new_min, new_limit)
        Database.Close_database()  # disconnect

        my_UI.Set_range()
        my_UI.team_box.setFocus()

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
