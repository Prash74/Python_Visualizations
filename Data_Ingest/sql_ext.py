import mysql.connector
import getpass

pwd = getpass.getpass("Enter Password: ")
try:
    cnx = mysql.connector.connect(user='root', database='employees',
                                  password=pwd)
    cursor = cnx.cursor()

    query = ("SELECT first_name, last_name, birth_date\
              FROM employees LIMIT 30")
    cursor.execute(query)
    for i in cursor:
        print i[0]
    cursor.close()
    cnx.close()
except:
    print "Connection Error. Wrong Username/Pwd"
