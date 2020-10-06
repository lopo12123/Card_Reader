pyinstaller -F -w [主文件] -p [子文件]
打包管理界面：pyinstaller -F -w Manage.py -p Database.py

==================================================
==================================================

Date: 2020/10/5

==================================================

Instructions for use:
  **** ****

==================================================

File tree directory:

- - - - - - - - - - - - - - - - - - - -
Project File

   | - database.db
   |
   | - Database.py
   |
   | - Manage.py
   |
   | - User.py
   |
   | - README.txt
   |
   | - Resources
   |
   |       | - Icon File
   |       |
   |       |     | - Icon1.png
   |       |     |
   |       |     | - Icon2.png
   |       |     |
   |       |     | - Icon3.png
   |       |
   |

- - - - - - - - - - - - - - - - - - - -

==================================================

Document explanation:

File Name: Database.py
Uasge: The 'Database.py' file is used to create the user database, and contains functions such as adding, deleting, checking and modifying database content.

File Name: Manage.py
Usage: The ‘Manage.py’ file is used to create an application for managing the card database. This application allows the administrator to view the information of the specified card or view the user information of all the cards in the database, and can modify the information of the selected user.

File Name: ***.py
Usage: ***

File Name: database.db
Usage: The 'database.db' file is a database file used to store the basic information of the card.

File Name: README.txt
Usage: The 'README.txt' file includes software function descriptions, operation and use methods, instructions for use, code directory structure and common problems and precautions.

File Name: Resources
Usage: The 'Resources' folder is used to store some material files.

==================================================

Note: 

1.The resource calls and database operations in the application use relative paths, so do not change the file tree structure in the 'project' folder to avoid the program`s failure to open or abnormal crashes.

2.The text box for entering the card number can only be used to enter numbers. Entering letters and text will cause errors.

==================================================
==================================================




