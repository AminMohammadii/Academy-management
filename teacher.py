from dbConnect import doQuery, tables


def teacher_panel(data):

    teacherID = find_teacher_id(data[0])

    available = {'A': "My classes",
                 'B': "Roll call students",
                 'C': "Grading students",
                 'D': "My students",
                 'E': "Teach new language"}

    # print()
    while True:
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        print("Success usually comes to those who are too busy looking for it."
              "\n What do you want to do today? \n")

        for key, value in available.items():
            print("\t", key, "-", value)

        choice = input("Enter a, b ,c... or exit : ").upper()
        print()
        if choice in available:
            if choice == 'A':
                teacher_classes(teacherID)
            if choice == 'B':
                students_call_roll(teacherID)
            if choice == 'C':
                grade_student()
            if choice == 'D':
                show_students(teacherID)
            if choice == 'E':
                add_new_language(teacherID)
        elif choice == "EXIT" or choice == 'Q':
            break
        else:
            print("Please enter valid amount!")


def teacher_classes(teacherID):
    print()

    sql = "SELECT * FROM {} WHERE teacher_id={}".format(tables["class"], teacherID)
    result, infos = doQuery(sql)

    for info in infos:
        print("class id:", info[0], "| language id:", info[2], "| start date:", info[3],
              "| end date:", info[4], "| sessions number:", info[5], "| term:", info[6])

        sql = "SELECT * FROM {} WHERE class_id = {}".format(tables["class_time"], info[0])
        result, classTimes = doQuery(sql)

        print("class time info:")
        for classTime in classTimes:
            print("\tclass time:", classTime[2], "| class date:", classTime[3], "| class room:", classTime[4])
        print("\n************************************\n")


def students_call_roll(teacherID):

    studentID = int(input("studentID: "))
    classTimeID = int(input("classTimeID: "))
    status = input("status: ")
    # date = input("date: ")
    description = input("description: ")

    if status == 0 or status == "False" or status == "false":
        status = 0
    else:
        status = 1

    sql = "INSERT INTO {}(teacher_id, student_id, class_time_id, status, description)" \
          " VALUES ('{}','{}','{}','{}', '{}')" \
        .format(tables["students_rollcall"], teacherID, studentID, classTimeID, status, description)
    result = doQuery(sql)

    if result[0]:
        print("\nrecord saved successfully")


def grade_student():
    studentID = int(input("studentID: "))
    classID = int(input("classID: "))
    grade = int(input("grade: "))

    sql = "UPDATE {} SET grade={} WHERE student_id={} AND class_id={}" \
        .format(tables["student_classes"], grade, studentID, classID)
    result = doQuery(sql)

    if result[0]:
        print("\nrecord saved successfully")


def show_students(teacherID):
    sql = "SELECT * FROM {} INNER JOIN {} ON {}.id=user_id WHERE {}.id IN " \
          "(SELECT student_id FROM {} INNER JOIN {} on class_id = {}.id WHERE teacher_id= {})" \
        .format(tables["student"], tables["user"], tables["user"], tables["student"],
                tables["student_classes"], tables["class"], tables["class"], teacherID)
    result, infos = doQuery(sql)

    print("your students list:")

    for info in infos:
        print("name:", info[5], info[6], "| id:", info[4], "| student id:", info[0], "| start date:", info[2],
              "| passed terms:", info[3],
              "| national code:", info[8], "| phone number:", info[9], "| address:", info[10])

    print("\n*****************************************\n")

def add_new_language(teacherID):
    languageID = input("languageID: ")
    degree = input("degree: ")
    sql = "INSERT INTO {}(teacher_id, teaching_language_id, degree)" \
          " VALUES ('{}','{}','{}')" \
        .format(tables["teacher_languages"], teacherID, languageID, degree)
    result = doQuery(sql)

    if result[0]:
        print("\nrecord saved successfully")


def find_teacher_id(user_id):
    sql = "SELECT id FROM {} WHERE user_id = {}".format(tables["teacher"], user_id)

    result = doQuery(sql)
    teacherID = int(result[1][0][0])
    return teacherID
