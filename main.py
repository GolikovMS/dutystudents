with open("students.txt", "r", encoding="utf-8") as students_file:
    students = students_file.read().splitlines()

already_duty_file = open("already_duty.txt", "r+", encoding="utf-8")
already_duty = already_duty_file.read().splitlines()

for student in students:
    if student not in already_duty:
        question = input(f"{student} не дежурил\nДобавить его в базу данных тех, кто уже отдежурил?\n"
                         f"Введите 'Да' или 'Нет': ").strip().lower()
        if question == "да":
            already_duty_file.write(f"{student}\n")
        print()
already_duty_file.close()
