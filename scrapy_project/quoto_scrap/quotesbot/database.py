import sqlite3

#https://sqliteonline.com/     open .db file here to check all content


#create database and connect
conn = sqlite3.connect("myquotes_latest.db")

# create cursor object
cursor = conn.cursor()
        #  excute query  for creating table

# cursor.execute("""create table quoto(
# title text,
# author text,
# tag text
# )""")

# executing query to insrt table

cursor.execute(""" insert into quoto values ("satish","kumar","gupta") """)



conn.commit()
conn.close()
