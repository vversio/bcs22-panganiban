passed = 0
failed = 0

s_records = [["Name", "Quiz 1", "Quiz 2", "Quiz 3", "Class Participation", "Final Exam", "Average", "Status"]]

while True:
    student = input("Student's Name: ")
    q1 = int(input("What is Student's Score in Q1: "))
    q2 = int(input("What is Student's Score in Q2: "))
    q3 = int(input("What is Student's Score in Q3: "))
    cp = int(input("What is Student's Class Participation: "))
    fl = int(input("What is Student's Score in Final Exam: "))

    f_grade = int((q1 + q2 + q3 + cp + fl) / 5)

    if f_grade >= 75:
        status = "PASSED"
        passed += 1
    else:
        status = "FAILED"
        failed += 1
      
    records2 = [student, q1, q2, q3, cp, fl, f_grade, status]

    s_records.append(records2)

    new = input("Do you want to add another student (yes/no): ")

    if new.lower() == "yes":
        continue
    elif new.lower() == "no":
        break
    else:
        print("INVALID")

for row in s_records:
    print("- {0:<20} - {1:<7} - {2:<7} - {3:<7} - {4:<20} - {5:<10} - {6:<7} - {7:<7} -".format(*row))

print("Total Passed:", passed)
print("Total Failed:", failed)
