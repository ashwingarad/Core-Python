import pymysql
conn = pymysql.connect(host='127.0.0.1', user='root', passwd='root', db='test')

cursor = conn.cursor(pymysql.cursors.DictCursor)

name = input('Enter name: ')
sql = "Select * from Student where fname = '{n}'".format(n=name)
try:
    cursor.execute(sql)
    if cursor.rowcount > 0:
        for c in cursor:
            print('\nFirst Name = ', c['fname'])
            print('Last Name = ', c['lname'])
            print('Mobile Number = ', c['mobile'])
            print('Gender = ', c['gender'])
            print('Marks = ', c['marks'])
    else:
        print('No records Found')
except Exception as e:
    print(e)
finally:
    cursor.close()
    conn.close()
