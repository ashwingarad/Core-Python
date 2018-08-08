import pymysql

conn = pymysql.connect(host='127.0.0.1', user='root', passwd='root', db='test')
cursor = conn.cursor()

# conn.insert_id()

fname = input('Enter First name : ')
lname = input('Enter Last name : ')
mobile = int(input('Enter Contact number : '))
gender = input('Enter Gender : ')
marks = int(input('Enter Marks : '))

sql = """INSERT INTO Student(id, fname, lname, mobile, gender, marks) 
    VALUES(NULL, "{fn}", "{ln}", "{mob}", "{gen}", "{m}");"""

# sql = "INSERT INTO Student(id, fname, lname, mobile, gender, marks) " + \
#     "VALUES(NULL, '{fn}', '{ln}', '{mob}', '{gen}', '{m}');"

sql_cmd = sql.format(fn=fname, ln=lname, mob=mobile, gen=gender, m=marks)
try:
    cursor.execute(sql_cmd)
    conn.commit()
    print('Record inserted')
except Exception as e:
    print(e)
    conn.rollback()

conn.close()
