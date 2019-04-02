import sqlite3

class DataBase:
	'''In memory database to hold option price and initial delta with ref as primary key'''

	def __init__(self):
		self.conn = sqlite3.connect(':memory:')
		self.c = self.conn.cursor()

		self.c.execute(""" CREATE TABLE data (
			
			ref integer,
			price float,
			delta float
			)""" )


	def insert_data(self, ref, price, delta):
		with self.conn:
			self.c.execute("INSERT INTO data VALUES (:ref, :price, :delta)",{'ref': ref, 'price': price, 'delta': delta})

	def get_data(self):
		with self.conn:
			 self.c.execute("SELECT * FROM data")
			 return self.c.fetchall()




