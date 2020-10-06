# -*- coding:utf-8 -*-
import sys
import Database
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLineEdit, QLabel, QListWidget, QMessageBox
from PyQt5.QtCore import QTimer, QDateTime, Qt


# UI interface
class UI(QWidget):
    # Setting parameters
    def __init__(self):
        super().__init__()
        self.pos_X = 300
        self.pos_Y = 200
        self.length = 650
        self.height = 750
        self.title = '管理系统'
        self.search_result = False  # Whether the query is successful
        self.select_result = False  # Whether any item is selected
        self.now_item = ''
        self.info = None
        self.initUI()  # init UI

    # Initialize the UI interface
    def initUI(self):
        '''Set location, title and icon'''
        # Set the position and size of the window
        # (pos_X, pos_Y, length, height)
        self.setGeometry(self.pos_X, self.pos_Y, self.length, self.height)

        # Set the title of the window
        self.setWindowTitle(self.title)

        # Set the icon of the window (if any)
        self.setWindowIcon(QIcon('./Resources/Icon/Icon1.png'))
        '''First line, title and time'''
        # Position: Upper left corner
        # Usage: Show title
        self.title_box = QLineEdit(self)
        self.title_box.resize(280, 30)
        self.title_box.move(30, 40)
        self.title_box.setAlignment(Qt.AlignCenter)
        self.title_box.setText('卡片用户管理')
        self.title_box.setFocusPolicy(Qt.NoFocus)  # Make it uneditable

        # Position: Upper right corner
        # Usage: Show data and time
        self.time_box = QLineEdit(self)
        self.time_box.resize(280, 30)
        self.time_box.move(340, 40)
        self.time_box.setAlignment(Qt.AlignCenter)
        self.time_box.setFocusPolicy(Qt.NoFocus)
        timer = QTimer(self)
        timer.timeout.connect(self.get_time)
        timer.start()
        '''Search prompt text and search box and two buttons'''
        # Text hint for search box
        self.search_text = QLabel(self)
        self.search_text.resize(280, 30)
        self.search_text.move(30, 100)
        self.search_text.setText('<h3>快速搜索框：</h3>')

        # Search box
        self.search_box = QLineEdit(self)
        self.search_box.resize(280, 30)
        self.search_box.move(30, 140)
        self.search_box.setPlaceholderText('请输入要查询的卡号或刷卡读取卡号')

        # Two buttons: search and show all
        # 'search' Button
        self.search_button = QPushButton('查询', self)
        self.search_button.setToolTip('查询当前卡号的卡片信息')
        self.search_button.resize(120, 30)
        self.search_button.move(340, 140)
        self.search_button.clicked.connect(self.Re_search_button)

        # 'show_all' Button
        self.show_all_button = QPushButton('显示全部', self)
        self.show_all_button.setToolTip('显示所有卡片的信息')
        self.show_all_button.resize(120, 30)
        self.show_all_button.move(500, 140)
        self.show_all_button.clicked.connect(self.Re_show_all_button)
        '''Result prompt text, result output list and information list'''
        # Text hint for result box
        self.result_text = QLabel(self)
        self.result_text.resize(280, 30)
        self.result_text.move(30, 200)
        self.result_text.setText('<h3>查询结果：</h3>')

        # Text hint for information box
        self.information_text = QLabel(self)
        self.information_text.resize(280, 30)
        self.information_text.move(340, 200)
        self.information_text.setText('<h3>卡片信息：</h3>')

        # Result list box
        self.result_box = QListWidget(self)
        self.result_box.resize(280, 350)
        self.result_box.move(30, 240)
        self.result_box.doubleClicked.connect(self.Re_list_left)

        # Arrow in the middle of the two lists
        self.arrow_text = QLabel(self)
        self.arrow_text.resize(20, 30)
        self.arrow_text.move(315, 400)
        self.arrow_text.setText('→')

        # Information list box
        self.information_box = QListWidget(self)
        self.information_box.resize(280, 350)
        self.information_box.move(340, 240)
        # Add the 'list box cannot be selected' function

        # New button
        self.new_button = QPushButton('添加卡片信息', self)
        self.new_button.setToolTip('添加新的卡片数据')
        self.new_button.resize(130, 40)
        self.new_button.move(65, 650)
        # An interface for adding new cards appears
        # Connect to the response function
        self.new_button.clicked.connect(self.Re_new_button)

        # Edit button
        self.edit_button = QPushButton('修改卡片信息', self)
        self.edit_button.setToolTip('修改当前选中的卡片的数据')
        self.edit_button.resize(130, 40)
        self.edit_button.move(260, 650)
        # An interface for modifying card information appears
        # Connect to the response function
        self.edit_button.clicked.connect(self.Re_edit_button)

        # Close button
        self.close_button = QPushButton('关闭管理系统', self)
        self.close_button.setToolTip('保存操作并关闭系统')
        self.close_button.resize(130, 40)
        self.close_button.move(455, 650)
        self.close_button.clicked.connect(self.close)  # close the window

    # Used to get the current time and display
    def get_time(self):
        datetime = QDateTime.currentDateTime()
        text = "当前时间：" + datetime.toString(Qt.ISODate)
        self.time_box.setText(text)

    # 'Search' button response function
    def Re_search_button(self):
        # Query the entered card number information from the database
        # Get the content in the text box
        search_id_text = self.search_box.text()
        self.result_box.clear()  # Clear the contents of the two lists first
        self.information_box.clear()
        if search_id_text:  # if the text box is not empty
            # Determine whether it is a number type
            id_result = is_number(search_id_text)
            if id_result is True:  # if it is a number type
                search_id = int(search_id_text)
                Database.Create_DB()  # connect DB to search
                if Database.Select_user(search_id) is None:
                    # No information about this card was found
                    self.result_box.addItem('没有查到此卡的信息！')
                    self.search_result = False
                    self.select_result = False
                else:
                    # Found the card information
                    # Then output the query result
                    self.result_box.addItem(search_id_text)
                    self.search_result = True
                    self.select_result = False
                # Disconnect from the database
                Database.Close_database()
            else:  # # if it is not a number type
                self.search_box.clear()
                self.Warning()
        else:  # if the search box is empty
            self.result_box.addItem('请输入查询的卡号！')
            self.search_result = False
            self.select_result = False

    # 'show_all' button response function
    def Re_show_all_button(self):
        # Query all tuples in the data sheet
        Database.Create_DB()  # connect DB to search
        all_tuples = Database.Select_all()
        Database.Close_database()  # Disconnect from the database
        self.search_box.clear()
        self.result_box.clear()  # Clear the contents of the list first
        self.information_box.clear()
        for item in all_tuples:
            self.result_box.addItem(str(item[0]))
            # print(item[0])
        self.search_result = True
        self.select_result = False

    # Responding to events after double-clicking the left list
    def Re_list_left(self):
        # Double-click an item in the list on the left
        # to open the corresponding information on the right
        self.now_item = self.result_box.currentItem().text()  # selected item
        # print(self.now_item)
        self.information_box.clear()  # Clear the contents of the list first
        if self.search_result is True:  # Search successful
            Database.Create_DB()
            self.info = Database.Select_user(int(self.now_item))
            Database.Close_database()
            self.information_box.addItem('卡号：' + str(self.info[0]))  # ID
            self.information_box.addItem('用户名：' + str(self.info[1]))  # NAME
            self.information_box.addItem('余额：' + str(self.info[2]))  # BALANCE
            self.select_result = True

    # 'new' button response function
    def Re_new_button(self):
        # Clear current page
        self.search_box.clear()
        self.result_box.clear()
        self.information_box.clear()
        # Clear the input box to enter new data
        my_UI_new.id_box.setText('')
        my_UI_new.name_box.setText('')
        my_UI_new.balance_box.setText('')
        my_UI_new.show()

    # 'edit' button response function
    def Re_edit_button(self):
        # If and only if you select an item in the list on the left,
        # a response will appear, and the modification interface will appear
        if my_UI.select_result:
            self.search_box.clear()
            self.result_box.clear()
            self.information_box.clear()
            my_UI_edit.id_box.setText(str(self.info[0]))
            my_UI_edit.name_box.setText(str(self.info[1]))
            my_UI_edit.balance_box.setText(str(self.info[2]))
            my_UI_edit.show()
        # else: QMessagebox

    '''
    # 'close' button response function
    def Re_close_button(self):
        # 补充：响应事件
        pass
    '''

    def Warning(self):
        self.reply = QMessageBox.question(self, '警告！', '请确认帐号为纯数字！', QMessageBox.Yes, QMessageBox.Yes)


# 'NEW' interface
# 'Edit' interface
class UI_NEW(QWidget):
    # Setting parameters
    def __init__(self):
        super().__init__()
        self.pos_X = 475
        self.pos_Y = 340
        self.length = 300
        self.height = 350
        self.title = '新建'
        self.new_id = ''  # Used to store new card information
        self.new_name = ''
        self.new_balance = ''
        self.initUI()  # init UI

    # Initialize the UI interface
    def initUI(self):
        '''Set location, title and icon'''
        # Set the position and size of the window
        # (pos_X, pos_Y, length, height)
        self.setGeometry(self.pos_X, self.pos_Y, self.length, self.height)

        # Set the title of the window
        self.setWindowTitle(self.title)

        # Set the icon of the window (if any)
        self.setWindowIcon(QIcon('./Resources/Icon/Icon2.png'))
        '''Card number, only display can not be modified'''
        self.id_text = QLabel(self)
        self.id_text.resize(70, 30)
        self.id_text.move(40, 40)
        self.id_text.setText('<h3>卡号:</h3>')

        self.id_box = QLineEdit(self)
        self.id_box.resize(150, 30)
        self.id_box.move(110, 40)
        self.id_box.setPlaceholderText('请刷卡读取卡号或输入新增的卡号')
        self.id_box.setToolTip('请刷卡读取卡号或输入新增的卡号')
        '''User name, can be modified'''
        self.name_text = QLabel(self)
        self.name_text.resize(70, 30)
        self.name_text.move(40, 110)
        self.name_text.setText('<h3>用户:</h3>')

        self.name_box = QLineEdit(self)
        self.name_box.resize(150, 30)
        self.name_box.move(110, 110)
        self.name_box.setPlaceholderText('请输入用户名')
        self.name_box.setToolTip('请输入用户名')
        '''Balance, can be modified'''
        self.balance_text = QLabel(self)
        self.balance_text.resize(70, 30)
        self.balance_text.move(40, 180)
        self.balance_text.setText('<h3>余额:</h3>')

        self.balance_box = QLineEdit(self)
        self.balance_box.resize(150, 30)
        self.balance_box.move(110, 180)
        self.balance_box.setPlaceholderText('请输入余额')
        self.balance_box.setToolTip('请输入余额，注意输入整数')
        '''Cancel and confirm buttons'''
        self.cancel_button = QPushButton('取消', self)
        self.cancel_button.setToolTip('取消新建')
        self.cancel_button.resize(100, 30)
        self.cancel_button.move(35, 280)
        self.cancel_button.clicked.connect(self.close)

        self.confirm_button = QPushButton('确认', self)
        self.confirm_button.setToolTip('确认并保存所有修改')
        self.confirm_button.resize(100, 30)
        self.confirm_button.move(165, 280)
        self.confirm_button.clicked.connect(self.Re_confirm_button)

    def Re_confirm_button(self):
        # Get new card information
        self.new_id = self.id_box.text()
        self.new_name = self.name_box.text()
        self.new_balance = self.balance_box.text()
        # If the three information is not empty, store it in the database
        if self.new_id != '' and self.new_name != '' and self.new_balance != '':
            if is_number(self.new_id) is True and is_number(self.new_balance) is True:
                if int(self.new_balance) < 0:
                    self.Warning_2()
                else:
                    Database.Create_DB()
                    Database.Insert_user(int(self.new_id), self.new_name, int(self.new_balance))
                    Database.Close_database()
                    self.close()
            else:
                self.Warning()

    def Warning(self):
        self.reply = QMessageBox.question(self, '警告！', '请确认卡号/余额为纯数字！', QMessageBox.Yes, QMessageBox.Yes)

    def Warning_2(self):
        self.reply = QMessageBox.question(self, '警告！', '请确认余额值非负！', QMessageBox.Yes, QMessageBox.Yes)


# 'Edit' interface
class UI_EDIT(QWidget):
    # Setting parameters
    def __init__(self):
        super().__init__()
        self.pos_X = 475
        self.pos_Y = 340
        self.length = 300
        self.height = 350
        self.title = '修改'
        self.select_id = ''  # Used to store new card information
        self.new_name = ''
        self.new_balance = ''
        self.initUI()  # init UI

    # Initialize the UI interface
    def initUI(self):
        '''Set location, title and icon'''
        # Set the position and size of the window
        # (pos_X, pos_Y, length, height)
        self.setGeometry(self.pos_X, self.pos_Y, self.length, self.height)

        # Set the title of the window
        self.setWindowTitle(self.title)

        # Set the icon of the window (if any)
        self.setWindowIcon(QIcon('./Resources/Icon/Icon3.png'))
        '''Card number, only display can not be modified'''
        self.id_text = QLabel(self)
        self.id_text.resize(70, 30)
        self.id_text.move(40, 40)
        self.id_text.setText('<h3>卡号:</h3>')

        self.id_box = QLineEdit(self)
        self.id_box.resize(150, 30)
        self.id_box.move(110, 40)
        self.id_box.setFocusPolicy(Qt.NoFocus)  # Make it uneditable
        '''User name, can be modified'''
        self.name_text = QLabel(self)
        self.name_text.resize(70, 30)
        self.name_text.move(40, 110)
        self.name_text.setText('<h3>用户:</h3>')

        self.name_box = QLineEdit(self)
        self.name_box.resize(150, 30)
        self.name_box.move(110, 110)
        '''Balance, can be modified'''
        self.balance_text = QLabel(self)
        self.balance_text.resize(70, 30)
        self.balance_text.move(40, 180)
        self.balance_text.setText('<h3>余额:</h3>')

        self.balance_box = QLineEdit(self)
        self.balance_box.resize(150, 30)
        self.balance_box.move(110, 180)
        '''Cancel and confirm buttons'''
        self.cancel_button = QPushButton('取消', self)
        self.cancel_button.setToolTip('取消所有修改')
        self.cancel_button.resize(100, 30)
        self.cancel_button.move(35, 280)
        self.cancel_button.clicked.connect(self.close)

        self.confirm_button = QPushButton('确认', self)
        self.confirm_button.setToolTip('确认并保存所有修改')
        self.confirm_button.resize(100, 30)
        self.confirm_button.move(165, 280)
        self.confirm_button.clicked.connect(self.Re_confirm_button)

    def Re_confirm_button(self):
        self.select_id = self.id_box.text()
        # Get new card information
        self.new_name = self.name_box.text()
        self.new_balance = self.balance_box.text()
        # If the two information is not empty, store it in the database
        if self.new_name != '' and self.new_balance != '':
            if is_number(self.new_balance) is True:
                if int(self.new_balance) < 0:
                    self.Warning_2()
                else:
                    Database.Create_DB()
                    Database.Update_user(int(self.select_id), self.new_name, int(self.new_balance))
                    Database.Close_database()
                    self.close()
            else:
                self.Warning()

    def Warning(self):
        self.reply = QMessageBox.question(self, '警告！', '请确认余额为纯数字！', QMessageBox.Yes, QMessageBox.Yes)

    def Warning_2(self):
        self.reply = QMessageBox.question(self, '警告！', '请确认余额值非负！', QMessageBox.Yes, QMessageBox.Yes)


def is_number(s):
    '''
    Function: is_number(s)
    Usage: Enter a string of characters to determine whether it is a number
    '''
    try:
        int(s)
        return True
    except ValueError:
        return False


if __name__ == '__main__':

    # QApplication is equivalent to the main function,
    # which is the entry point of the program
    app = QApplication(sys.argv)

    # UI interface instantiation
    my_UI = UI()

    # 'new' interface instantiation
    my_UI_new = UI_NEW()

    # 'edit' interface instantiation
    my_UI_edit = UI_EDIT()

    # Show main interface
    my_UI.show()

    # Call the exit exit method of the sys library,
    # the condition is app.exec_() (that is, the entire window is closed)
    sys.exit(app.exec_())
