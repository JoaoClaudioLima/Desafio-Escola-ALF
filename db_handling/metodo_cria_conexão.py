import sqlite3
from sqlite3 import Error

#Cria uma conexão com a database especificada pelo argumento.
def create_connection(database):
	conn = None
	try:
		conn = sqlite3.connect(database)
	except Error as e:
		print(e)
	return conn