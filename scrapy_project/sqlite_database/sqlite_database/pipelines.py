# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import sqlite3

class SqliteDatabasePipeline(object):

	def __init__(self):
		print("init---------------")

		self.create_connection()
		self.create_table()

	def create_table(self):
		print("creating table---------------")
		self.cursor.execute("""  DROP TABLE IF EXISTS quoto_tb11 """)
		self.cursor.execute("""create table quoto_tb11(
            title text
           )""")

	def create_connection(self):
		print("creating connection---------------")

		self.conn = sqlite3.connect("quoto135.db")
		self.cursor = self.conn.cursor()

	def store_into_db(self):
		print("store into db---------------")
		self.cursor.execute(""" insert into quoto_tb11(title) values(?);
			""",
			("satish",)) # , is mendatory if there is only data.. tuple decalaration
		self.conn.commit()


	def process_item(self, item, spider):
		print("process item-------------------")
		self.store_into_db()
    	return item
# conn.execute("insert into crawled (title, body) values (?, ?);",(title, body))