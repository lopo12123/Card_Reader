# -*- coding:utf-8 -*-
import sys
import Database
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLineEdit, QLabel, QListWidget
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
        self.search_result = False
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
        self.setWindowIcon(QIcon('./Resources/Icon1.png'))
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
        self.search_button.resize(120, 30)
        self.search_button.move(340, 140)
        self.search_button.clicked.connect(self.Re_search_button)

        # 'show_all' Button
        self.show_all_button = QPushButton('显示全部', self)
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
        # 补充：响应事件

        # New button
        self.new_button = QPushButton('添加卡片信息', self)
        self.new_button.setToolTip('添加新的卡片数据')
        self.new_button.resize(130, 40)
        self.new_button.move(65, 650)

        # Edit button
        self.edit_button = QPushButton('修改卡片信息', self)
        self.edit_button.setToolTip('修改当前选中的卡片的数据')
        self.edit_button.resize(130, 40)
        self.edit_button.move(260, 650)

        # Close button
        self.close_button = QPushButton('关闭管理系统', self)
        self.close_button.setToolTip('保存操作并关闭系统')
        self.close_button.resize(130, 40)
        self.close_button.move(455, 650)

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
        self.result_box.clear()  # Clear the contents of the list first
        self.information_box.clear()
        if search_id_text:  # If the text box is not empty
            search_id = int(search_id_text)
            Database.Create_DB()  # connect DB to search
            if Database.Select_user(search_id) is None:
                # No information about this card was found
                self.result_box.addItem('没有查到此卡的信息！')
                self.search_result = False
            else:
                # Found the card information
                # Then output the query result
                self.result_box.addItem(search_id_text)
                self.search_result = True
            # Disconnect from the database
            Database.Close_database()
        else:
            self.result_box.addItem('请输入查询的卡号！')
            self.search_result = False

    # 'show_all' button response function
    def Re_show_all_button(self):
        # Query all tuples in the data sheet
        Database.Create_DB()  # connect DB to search
        all_tuples = Database.Select_all()
        Database.Close_database()  # Disconnect from the database
        self.result_box.clear()  # Clear the contents of the list first
        self.information_box.clear()
        for item in all_tuples:
            self.result_box.addItem(str(item[0]))
            # print(item[0])
        self.search_result = True

    # Responding to events after double-clicking the left list
    def Re_list_left(self):
        # Double-click an item in the list on the left
        # to open the corresponding information on the right
        now_item = self.result_box.currentItem().text()  # Get selected item
        # print(now_item)
        self.information_box.clear()  # Clear the contents of the list first
        if self.search_result is True:  # Search successful
            Database.Create_DB()
            info = Database.Select_user(int(now_item))
            Database.Close_database()
            self.information_box.addItem('卡号：' + str(info[0]))  # ID
            self.information_box.addItem('用户名：' + str(info[1]))  # NAME
            self.information_box.addItem('余额：' + str(info[2]))  # BALANCE

    # 'new' button response function
    def Re_new_button(self):
        # 补充：响应事件
        pass

    # 'edit' button response function
    def Re_edit_button(self):
        # 补充：响应事件
        pass

    # 'close' button response function
    def Re_close_button(self):
        # 补充：响应事件
        pass


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
