import mysql.connector.pooling as pooling
from config import DBHOST, DBPASS, DBPORT, DBUSER


MySQLError = pooling.errors.PoolError
dbconfig = {"username": DBUSER, "host": DBHOST, "passwd": DBPASS, "port": DBPORT,"pool_size":30}
#con = connection.MySQLConnection(**dbconfig)
pool = pooling.MySQLConnectionPool(**dbconfig)
