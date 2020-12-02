# -*- coding:utf-8 -*-
import sqlite3


def Create_DB():
    global my_cursor, my_database

    # connect to the database and get the cursor
    DB_name = 'database.db'
    my_database = sqlite3.connect(DB_name)
    my_cursor = my_database.cursor()


def Create_user():  # checked
    '''
    Function: Create_user()
    Usage: Create the 'USER' table
    Note: The format of the table is as follows.
    * TABLE NAME: USER
    * -----------------------------------------------------------
      | Columns   |   Type    |   NN  |   PK  |   Default Value |
      | ID        |   INT     |   √   |   √   |   NULL          |
      | NAME      |   CHAR    |   √   |       |   NULL          |
      | BALANCE   |   INT     |   √   |       |   NULL          |
      | RATE_NOW  |   INT     |   √   |       |   1             |
      | RATE_NEXT |   INT     |   √   |       |   1             |
      -----------------------------------------------------------
    '''

    my_cursor.execute('''
        CREATE TABLE IF NOT EXISTS USER(
            ID INT PRIMARY KEY NOT NULL,
            NAME CHAR NOT NULL,
            BALANCE INT NOT NULL,
            RATE_NOW INT NOT NULL,
            RATE_NEXT INT NOT NULL
        );''')

    my_cursor.execute('''
        CREATE TABLE IF NOT EXISTS SETTING(
            NUMBER INT PRIMARY KEY NOT NULL,
            MY_MAX INT NOT NULL,
            MY_MIN INT NOT NULL,
            MY_LIMIT INT NOT NULL
        );''')

    my_cursor.execute('''
        CREATE TABLE IF NOT EXISTS OPERATE(
            NUMBER INT PRIMARY KEY NOT NULL,
            CANCEL INT NOT NULL,
            OPERATION VARCHAR NOT NULL,
            PLAYER1 INT,
            PLAYER2 INT,
            AMOUNT DOUBLE
        );''')


def Insert_user(user_id, user_name, user_balance):  # checked
    '''
    Function: Insert_user(user_id, user_name, user_balance)
    Usage: Add a new user (ie a new tuple) to the data sheet 'USER'.
    Note: The three parameters represent the id, name and balance respectively.
    '''

    insert_id = user_id  # Receive three new data
    insert_name = user_name
    insert_balance = user_balance
    my_cursor.execute('''INSERT INTO USER VALUES(?, ?, ?, 1, 1);''',
                      (insert_id, insert_name, insert_balance))


def Delete_user(user_id):  # checked
    '''
    Function: Delete_user(user_id)
    Usage: Delete a specific user (ie a specific tuple) in data sheet 'USER'.
    Note: The required parameter is the 'user_id',
          which is the primary key of the tuple.
    '''

    delete_id = user_id  # Receive the id of the user to be deleted
    my_cursor.execute('''DELETE FROM USER WHERE ID = ?;''', [(delete_id)])


def Select_user(user_id):  # checked
    '''
    Function: Select_user(user_id)
    Usage: Find a specific tuple based on the user id
           (that is, the primary key of the tuple),
           and return balance information.
    Note: The required parameter is the user id,
          which is the primary key of the tuple.
    '''

    select_id = user_id
    my_cursor.execute('''SELECT * FROM USER WHERE ID = ?;''', [(select_id)])

    for item in my_cursor.fetchall():
        return item

    # the result of 'my_cursor.fetchall()' is like [(1, 'A', 200)]
    # (1)print(my_cursor.fetchall())

    # the result of 'item' is like (1, 'A', 200)
    # (2)for item in my_cursor.fetchall():
    # (2)    print(item)


def Select_all():  # checked
    '''
    Function: Select_all()
    Usage: Query all tuples in the data sheet and return
    Note: The returned data type is dictionary type
    '''

    my_cursor.execute('''SELECT * FROM USER;''')
    # print(my_cursor.fetchall())
    return my_cursor.fetchall()


def Update_one(user_id, new_balance):  # checked
    update_id = user_id
    update_balance = new_balance
    my_cursor.execute('''UPDATE USER SET BALANCE = ? WHERE ID = ?;''',
                      (update_balance, update_id))


def Update_rate(user_id, rate_next):  # checked
    '''
    About 'RATE':
    1 - normal;
    2 - double add;
    3 - half add;
    4 - double sub;
    5 - half sub;
    '''

    update_id = user_id
    update_rate = rate_next
    my_cursor.execute('''UPDATE USER SET RATE_NEXT = ? WHERE ID = ?;''',
                      (update_rate, update_id))


def Next_term():
    '''
    rate_now = rate_next
    rate_next = 1(default)
    '''
    my_cursor.execute('''UPDATE USER SET RATE_NOW = RATE_NEXT;''')
    my_cursor.execute('''UPDATE USER SET RATE_NEXT = 1;''')


def Reset_rate():  # checked
    '''
    reset all the rate to '1'
    '''
    my_cursor.execute('''UPDATE USER SET RATE_NOW = 1;''')
    my_cursor.execute('''UPDATE USER SET RATE_NEXT = 1;''')


def Update_user(user_id, new_name, new_balance):  # checked
    '''
    Function: Update_user(user_id)
    Usage: Update the attribute information of the tuple,
           here specifically refers to changing the balance data.
    Note: The required parameter is the 'user_id',
          which is the primary key of the tuple.
    '''

    # Receive the id of the user who needs to
    # be modified and the new username and balance
    update_id = user_id
    update_name = new_name
    update_balance = new_balance
    my_cursor.execute(
        '''UPDATE USER SET NAME = ?, BALANCE = ? WHERE ID = ?;''',
        (update_name, update_balance, update_id))


def Get_Setting():
    my_cursor.execute('''SELECT * FROM SETTING;''')
    # print(my_cursor.fetchall())
    return my_cursor.fetchall()


def New_Setting(new_max, new_min, new_limit):
    my_cursor.execute(
        '''UPDATE SETTING SET MY_MAX = ?, MY_MIN = ?, MY_LIMIT = ? WHERE NUMBER = ?;''',
        (new_max, new_min, new_limit, 1))


def New_operate(my_num, my_cancel, my_text, my_p1=None, my_p2=None, my_amount=0):
    '''my_num: (private key) number;
    my_cancel: (0 / 1) 0: cant be cancelled / 1: can be cancelled
    my_text: the full operation record
    my_p1/my_p2: the players(if any)
    my_amount: the amount(if any)'''

    my_cursor.execute(
        '''INSERT INTO OPERATE VALUES(?, ?, ?, ?, ?, ?);''', (my_num, my_cancel, my_text, my_p1, my_p2, my_amount)
    )


def Get_operate():
    '''get a record'''
    my_cursor.execute('''SELECT * FROM OPERATE;''')
    # print(my_cursor.fetchall())
    return my_cursor.fetchall()


def Get_operate_record(record_num):
    '''get the record with record number record_num'''
    my_cursor.execute('''SELECT * FROM OPERATE WHERE NUMBER = ?;''', [(record_num)])
    return my_cursor.fetchall()[0]


def Delete_operate_record(record_num):
    '''delete the record with record number record_num'''
    my_cursor.execute('''DELETE FROM OPERATE WHERE NUMBER = ?;''', [(record_num)])


def Delete_operate():
    # cause there is no 'truncate' in sqlite3
    # so that we use delete instead
    my_cursor.execute('''DELETE FROM OPERATE''')


def Close_database():  # checked
    '''
    Function: close_database()
    Usage: 1 close the cursor,
           2 commit the transaction,
           3 close the connection.
    Note: After operating the database, you should commit
          the transaction and then close the connection.
    '''

    my_cursor.close()
    my_database.commit()
    my_database.close()


if __name__ == '__main__':
    '''
    If it is the main execution script,
    the following code will be executed,
    and it will not be executed as the called library
    '''

    Create_DB()  # connect DB
    Create_user()  # create sheet

    # my_cursor.execute('''INSERT INTO SETTING VALUES(1, 20000, 0, 5000);''')

    '''
    # test
    Insert_user(1, 'test1', 5000)
    Insert_user(2, 'test2', 5000)
    Insert_user(3, 'test3', 5000)
    Insert_user(4, 'test4', 5000)
    Insert_user(5, 'test5', 5000)
    Insert_user(6, 'test6', 5000)
    Insert_user(7, 'test7', 5000)
    Insert_user(8, 'test8', 5000)
    Insert_user(9, 'test9', 5000)
    Insert_user(10, 'test10', 5000)
    Insert_user(11, 'test11', 5000)
    Insert_user(12, 'test12', 5000)
    Insert_user(13, 'test13', 5000)
    Insert_user(14, 'test14', 5000)
    Insert_user(15, 'test15', 5000)
    Insert_user(16, 'test16', 5000)
    '''

    '''
    New_operate(1, 1, '第1条记录', 1, 2, 500)
    New_operate(2, 1, '第2条记录', 1, 2, 500)
    New_operate(3, 0, 'next round')
    New_operate(4, 1, '第3条记录', 2, 3, 500)
    '''

    '''a = Get_operate()
    for item in a:
        if item[1] == 1:
            print(item[2])
        else:
            print('can be canceled')'''

    # Delete_operate_record(12)
    # a = Get_operate_record(1)
    # print(a)

    Close_database()
