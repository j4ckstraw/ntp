import mysql.connector
from mysql.connector import errorcode

config = {
  'user': 'root',
  'password': 'ubuntu',
  'host': '127.0.0.1',
  'database': 'ntp',
  'raise_on_warnings': True,
}

try:
  cnx = mysql.connector.connect(**config)
  print('Connect ok!')
except mysql.connector.Error as err:
  if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
    print("Something is wrong with your user name or password")
  elif err.errno == errorcode.ER_BAD_DB_ERROR:
    print("Database does not exist")
  else:
    print(err)
else:
  cnx.close()
