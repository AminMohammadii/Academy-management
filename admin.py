from dbConnect import doQuery, tables


def admin_panel(data):

    adminID = find_admin_id(data[0])



    available = {'A': "Create new class",
                 'B': "Add new teacher",
                 'C': "Add new student",
                 'D': "Update class time/room",
                 'E': "Add teacher to class",
                 'F': "Add student to class",
                 'G': "Show classes",
                 'H': "Show teachers",
                 'I': "Show students",
                 'J': "Roll call of teachers",
                 'K': "Roll call of students"}
    while True:
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        print("We are not our best intentions. We are what we do."
              "\nWhat do you want to do today?")

        for key, value in available.items():
            print("\t", key, "-", value)

        choice = input("Enter a, b ,c... or exit: ").upper()
        print()
        if choice in available:
            # print("Accept")
            if choice == 'A':
                create_new_class()
            if choice == 'B':
                new_teacher()
            if choice == 'C':
                new_student()
            if choice == 'D':
                update_time_room()
            if choice == 'E':
                assign_teacher_to_class()
            if choice == 'F':
                assign_student_to_class()
            if choice == 'G':
                show_classes()
            if choice == 'H':
                show_teachers()
            if choice == 'I':
                show_students()
            if choice == 'J':
                teachers_call_roll(adminID)
            if choice == 'K':
                students_call_roll(adminID)
        elif choice == "EXIT" or choice == 'Q':
            break
        else:
            print("Please enter valid amount!")


def create_new_class():
    teacherID = input("\nteacherID: ")
    languageID = input("languageID: ")
    startDate = input("startDate: ")
    endDate = input("endDate: ")
    sessionsNumber = int(input("sessionsNumber: "))
    term = input("term: ")

    sql = "INSERT INTO {}(teacher_id, language_id, sessions_number, term)" \
          " VALUES ('{}','{}','{}','{}')"\
        .format(tables["class"], teacherID, languageID, sessionsNumber, term)

    result = doQuery(sql)
    if result[0]:
        print("\nClass added successfully")


def new_teacher():
    userID = new_user("teacher")
    startDate = input("startDate: ")
    endDate = input("endDate: ")

    sql = "INSERT INTO {}(user_id) VALUES ('{}')".format(tables["teacher"], userID)
    result = doQuery(sql)

    if result[0]:
        print("\nteacher added successfully")

    # print(userID)


def new_student():
    userID = new_user("student")
    startDate = input("startDate: ")
    passedTerms = int(input("passedTerms: "))

    sql = "INSERT INTO {}(user_id, passed_terms) VALUES ('{}','{}')"\
        .format(tables["student"], userID, passedTerms)
    result = doQuery(sql)

    if result[0]:
        print("\nstudent added successfully")


def new_user(role):
    firstName = input("firstName: ")
    lastName = input("lastName: ")
    nationalCode = input("nationalCode: ")
    phoneNumber = input("phoneNumber: ")
    address = input("address: ")

    sql = "INSERT INTO {}(first_name, last_name, role, national_code, phone_number, address)" \
          " VALUES ('{}','{}','{}','{}', '{}','{}')"\
        .format(tables["user"], firstName, lastName, role, nationalCode, phoneNumber, address)

    result = doQuery(sql)

    if result[0]:

        sql = "SELECT id FROM {} WHERE national_code = '{}'".format(tables["user"], nationalCode)
        # sql = "select LAST_INSERT_ID()"
        result = doQuery(sql)

        user_id = int(result[1][0][0])
        return user_id


def update_time_room():
    classID = input("classID: ")
    classTime = input("classTime: ")
    classDate = input("classDate: ")
    classRoom = input("classRoom: ")

    sql = "INSERT INTO {}(class_id, class_time, class_date, class_room)" \
          " VALUES ('{}','{}', '{}', '{}')"\
        .format(tables["class_time"], classID, classTime, classDate, classRoom)

    result = doQuery(sql)
    if result[0]:
        print("\nclass time/room updated successfully")


def assign_teacher_to_class():
    teacherID = input("teacherID: ")
    classID = input("classID: ")

    sql = "UPDATE {} SET teacher_id = {} WHERE id = {}"\
        .format(tables["class"], teacherID, classID)

    result = doQuery(sql)
    if result[0]:
        print("\nteacher added to class successfully")


def assign_student_to_class():
    studentID = input("studentID: ")
    classID = input("classID: ")

    sql = "INSERT INTO {}(student_id, class_id) VALUES ('{}','{}')"\
        .format(tables["student_classes"], studentID, classID)

    result = doQuery(sql)
    if result[0]:
        print("\nstudent added to class successfully")


def show_classes():
    sql = "SELECT * FROM {}".format(tables["class"])
    result, infos = doQuery(sql)

    for info in infos:
        print("id:", info[0], "| teacher id:", info[1], "| language id:", info[2], "| start date:", info[3],
              "| end date:", info[4], "| sessions number:", info[5], "| term:", info[6])

        sql = "SELECT * FROM {} WHERE class_id = {}".format(tables["class_time"], info[0])
        result, classTimes = doQuery(sql)

        print("class time info:")
        for classTime in classTimes:
            print("\tclass time:", classTime[2], "| class date:", classTime[3], "| class room:", classTime[4])
        print("\n************************************\n")


def show_teachers():
    sql = "SELECT * FROM {} INNER JOIN {} ON {}.id = user_id".format(tables["teacher"], tables["user"], tables["user"])

    result, infos = doQuery(sql)
    for info in infos:
        print("name:", info[5], info[6], "| id:", info[4], "| teacher id:", info[0], "| start_date:", info[2], "| end_date:", info[3],
              "| national code:", info[8], "| phone number:", info[9], "| address:", info[10])

        sql = "SELECT * FROM {} WHERE teacher_id = {}".format(tables["teacher_languages"], info[0])
        result, teachingLanguages = doQuery(sql)

        print("\n{} {} teaching languages:".format(info[5], info[6]))

        for teachingLanguage in teachingLanguages:
            print("\tlanguage:", teachingLanguage[2], "| degree:", teachingLanguage[3])

        sql = "SELECT * FROM {} WHERE teacher_id = {}".format(tables["class"], info[0])
        result, teacherClasses = doQuery(sql)

        print("\n{} {} classes:".format(info[5], info[6]))

        for tc in teacherClasses:
            print("class id:", tc[0],  "| language id:", tc[2], "| start date:", tc[3],
                  "| end date:", tc[4], "| sessions number:", tc[5], "| term:", tc[6])

        print("\n*********************************************\n")


def show_students():
    sql = "SELECT * FROM {} INNER JOIN {} ON {}.id = user_id".format(tables["student"], tables["user"], tables["user"])

    result, infos = doQuery(sql)
    for info in infos:
        # print(info)
        print("name:", info[5], info[6], "| id:", info[4], "| student id:", info[0], "| start date:", info[2],
              "| passed terms:", info[3],
              "| national code:", info[8], "| phone number:", info[9], "| address:", info[10])

        # continue
        sql = "SELECT * FROM {} WHERE student_id = {}".format(tables["student_classes"], info[0])
        result, studentClasses = doQuery(sql)

        print("\n{} {} classes:".format(info[5], info[6]))

        for sc in studentClasses:
            print("class id:", sc[2], "| grade:", sc[3])

        print("\n*********************************************\n")


def teachers_call_roll(adminID):
    teacherID = int(input("teacherID: "))
    classTimeID = int(input("classTimeID: "))
    status = input("status: ")
    # date = input("date: ")
    description = input("description: ")

    if status == 0 or status == "False" or status == "false":
        status = 0
    else:
        status = 1

    sql = "INSERT INTO {}(admin_id, teacher_id, class_time_id, status, description)" \
          " VALUES ('{}','{}','{}','{}', '{}')"\
        .format(tables["teachers_rollcall"], adminID, teacherID, classTimeID, status, description)
    result = doQuery(sql)

    if result[0]:
        print("\nrecord saved successfully")


def students_call_roll(adminID):
    studentID = int(input("studentID: "))
    classTimeID = int(input("classTimeID: "))
    status = input("status: ")
    # date = input("date: ")
    description = input("description: ")

    if status == 0 or status == "False" or status == "false":
        status = 0
    else:
        status = 1

    sql = "INSERT INTO {}(admin_id, student_id, class_time_id, status, description)" \
          " VALUES ('{}','{}','{}','{}', '{}')"\
        .format(tables["students_rollcall"], adminID, studentID, classTimeID, status, description)
    result = doQuery(sql)

    if result[0]:
        print("\nrecord saved successfully")


def find_admin_id(user_id):
    sql = "SELECT id FROM {} WHERE user_id = {}".format(tables["admin"], user_id)

    result = doQuery(sql)
    adminID = int(result[1][0][0])
    return adminID

