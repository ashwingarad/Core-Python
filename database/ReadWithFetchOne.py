import pymysql
conn = pymysql.connect(host='127.0.0.1', user='root', passwd='root', db='test')
cursor = conn.cursor()
gen = input('Enter Gender: ')
sql = "Select * from Student where gender = '{n}'".format(n=gen)
try:
    cursor.execute(sql)
    row = cursor.fetchone()    
    if cursor.rowcount > 0:
        while row is not None:
            print('\nFirst Name = ', row[1])
            print('Last Name = ', row[2])
            print('Mobile Number = ', row[3])
            print('Gender = ', row[4])
            print('Marks = ', row[5])
            
            row = cursor.fetchone()
    else:
        print('No records Found')
except Exception as e:
    print(e)
finally:
    cursor.close()
    conn.close()
