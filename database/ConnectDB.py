import pymysql
conn = pymysql.connect(host='127.0.0.1', user='root', passwd='root', db='test')
cursor = conn.cursor()
cursor.execute("SELECT * FROM employee")
for r in cursor:
    print(r)
cursor.close()
conn.close()
