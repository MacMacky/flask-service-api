import mysql.connector as connection
from settings import DBHOST, DBPASS, DBPORT, DBUSER


MySQLError = connection.Error
dbconfig = {"username": DBUSER, "host": DBHOST, "passwd": DBPASS, "port": DBPORT}
con = connection.MySQLConnection(**dbconfig)

