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
      -----------------------------------------------------------
    '''

    my_cursor.execute('''
        CREATE TABLE IF NOT EXISTS USER(
            ID INT PRIMARY KEY NOT NULL,
            NAME CHAR NOT NULL,
            BALANCE INT NOT NULL
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
    my_cursor.execute('''INSERT INTO USER VALUES(?, ?, ?);''',
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


def Select_all():
    '''
    Function: Select_all()
    Usage: Query all tuples in the data sheet and return
    Note: The returned data type is dictionary type
    '''

    my_cursor.execute('''SELECT * FROM USER;''')
    return my_cursor.fetchall()
    # print(my_cursor.fetchall())


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

    # test
    Create_DB()
    Create_user()
    '''
    Insert_user(1, 'one', 111)
    Insert_user(2, 'two', 222)
    Insert_user(3, 'three', 333)
    '''
    Select_all()
    Close_database()
