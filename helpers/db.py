import mysql.connector as connection
from settings import DBHOST,DBPASS,DBPORT,DBUSER


MySQLError = connection.Error
con = connection.connect(host=DBHOST,port=DBPORT,user=DBUSER,password=DBPASS)