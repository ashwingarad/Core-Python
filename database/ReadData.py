import pymysql

conn = pymysql.connect(host='127.0.0.1', user='root', passwd='root', db='test')

cursor = conn.cursor()
name = input('Enter name: ')
sql = "Select * from Student where fname = '{n}'".format(n=name)

cursor.execute(sql)

row = cursor.fetchall()
if row is not None:
    for c in row :
        print('First Name = ', c[1])
        print('Last Name = ', c[2])
        print('Mobile Number = ', c[3])
        print('Gender = ', c[4])
else:
    print('No record found')
    
conn.close()
