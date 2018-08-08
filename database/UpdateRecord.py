import pymysql
conn = pymysql.connect(host='127.0.0.1', user='root', passwd='root', db='test')

i = int(input('Enter id of student : '))
mob = int(input('Enter new Contact number : '))

sql = "Update Student set mobile = '{m}' where id = '{id}'".format(m=mob, id=i)

cursor = conn.cursor(pymysql.cursors.DictCursor)
try:
    with cursor:
        cursor.execute(sql)
        conn.commit()
        n = conn.affected_rows()
        if n > 0:
            print('Record successfully updated....')
        else:
            print('Something went wrong..!')
except Exception as e:
    print(e)
finally:
    conn.close()
