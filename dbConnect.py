import pymysql

tables = {
    "admin": "admin",
    "class": "class",
    "class_time": "class_time",
    "student": "student",
    "students_rollcall": "students_rollcall",
    "student_classes": "student_classes",
    "teacher": "teacher",
    "teachers_rollcall": "teachers_rollcall",
    "teacher_classes": "teacher_classes",
    "teacher_languages": "teacher_languages",
    "user": "user",
}

def doQuery(sql="SELECT * FROM user WHERE id='1'", fetch_num=0):

    HOSTNAME = 'localhost'
    USERNAME = 'root'
    PASSWORD = ''
    DATABASE = 'academy'

    myConnection = pymysql.connect(host=HOSTNAME, user=USERNAME, passwd=PASSWORD, db=DATABASE)

    cur = myConnection.cursor()

    # cur.execute("SELECT id, first_name, last_name FROM user")
    # result = cur.execute("SELECT * FROM user WHERE id='1'")
    result = cur.execute(sql)
    myConnection.commit()
    # for id, firstname, lastname in cur.fetchall():
    # for detail in cur.fetchall():
    # print(id, firstname, lastname)
    # print(detail)
    myConnection.close()
    if fetch_num:
        return result, cur.fetchone()

    return result, cur.fetchall()

# doQuery(myConnection)
