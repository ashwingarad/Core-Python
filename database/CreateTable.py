import pymysql
conn = pymysql.connect(host='127.0.0.1', user='root', passwd='root', db='test')
cursor = conn.cursor()

cursor.execute("DROP TABLE IF EXISTS STUDENT")

sql = """
        create table Student (id BIGINT PRIMARY KEY NOT NULL AUTO_INCREMENT, fname varchar(20), 
        lname varchar(20), mobile BIGINT, gender varchar(20), marks int)
"""
cursor.execute(sql)

conn.close()
print('Database created')