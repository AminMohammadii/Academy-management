from dbConnect import doQuery, tables


def student_panel(data):

    studentID = find_studentIid(data[0])

    available = {'A': "term classes and grades",
                 'B': "Classes attend history"}

    while True:

        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        print("You are never too old to set another goal or to dream a new dream."
              "\n What do you want to do today? \n")

        for key, value in available.items():
            print("\t", key, "-", value)

        choice = input("\nEnter a, b or exit: ").upper()
        print()
        if choice in available:
            if choice == 'A':
                class_detail(studentID)
            if choice == 'B':
                print("\nclasses which you were:")
                class_attend_history(studentID, True)
                print("classes which you were not:")
                class_attend_history(studentID, False)

        elif choice == "EXIT" or choice == 'Q':
            break
        else:
            print("Please enter valid amount!")


def class_detail(studentID):
    term = input("term: ")

    sql = "SELECT {}.class_id,teacher_id, language_id, start_date, end_date, sessions_number, grade FROM " \
          "{} INNER JOIN {} ON class_id={}.id  WHERE student_id = {} AND term = {}"\
        .format(tables["student_classes"], tables["student_classes"], tables["class"], tables["class"], studentID, term)

    result, infos = doQuery(sql)

    for info in infos:
        print("class id:", info[0], "| teacher id:", info[1], "| language id:", info[2], "| start_date:", info[3],
              "| end_date:", info[4], "| sessions_number:", info[5], "| grade:", info[6])

        sql = "SELECT * FROM {} WHERE class_id = {}".format(tables["class_time"], info[0])
        result, classTimes = doQuery(sql)

        print("class time info:")
        for classTime in classTimes:
            print("\tclass time:", classTime[2], "| class date:", classTime[3], "| class room:", classTime[4])
        print("\n************************************\n")


def class_attend_history(studentID, status):
    sql = "SELECT * FROM {} WHERE id IN(SELECT class_time_id FROM {} WHERE student_id= {} AND status = {})"\
        .format(tables["class_time"], tables["students_rollcall"], studentID, status)

    # print(sql)

    result, infos = doQuery(sql)
    for info in infos:
        print("class_id", info[1], "| class date:", info[3], "| class time:", info[2], "| class room:", info[4])
    print("\n**************************************")
    # print(infos)


def find_studentIid(user_id):
    sql = "SELECT id FROM {} WHERE user_id = {}".format(tables["student"], user_id)

    result = doQuery(sql)
    studentID = int(result[1][0][0])
    return studentID
