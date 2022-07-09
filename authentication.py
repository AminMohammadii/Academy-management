from dbConnect import doQuery
from admin import admin_panel
from teacher import teacher_panel
from student import student_panel


def authenticate():

    while True:

        user_id = int(input("WELCOME, please enter your id (type 0 to exit): "))

        if user_id == 0:
            break

        sql = "SELECT * FROM user WHERE id='{}'".format(user_id)
        is_exist, info = doQuery(sql, 1)

        if is_exist:
            role = info[3]

            print("\nWelcome to the app {} {}".format(info[1], info[2]))

            if role == "admin":
                admin_panel(info)

            elif role == "teacher":
                teacher_panel(info)

            elif role == "student":
                student_panel(info)

            else:
                print("your role has not any kind of access!")

        else:
            print("ID is invalid")
