import pymysql
conn = pymysql.connect(host='127.0.0.1', user='root', passwd='root', db='test')
cursor = conn.cursor()
name = input('Enter name: ')
sql = "Select * from Student where fname = '{n}'".format(n=name)
try:
    cursor.execute(sql)
    rows = cursor.fetchall()
    if cursor.rowcount > 0:
        for c in rows:
            print('\nFirst Name = ', c[1])
            print('Last Name = ', c[2])
            print('Mobile Number = ', c[3])
            print('Gender = ', c[4])
            print('Marks = ', c[5])
    else:
        print('No records Found')
except Exception as e:
    print(e)
finally:
    cursor.close()
    conn.close()
