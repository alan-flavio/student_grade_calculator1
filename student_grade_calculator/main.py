import os
import csv
from utills.student import Student


def load_student_data(filename):
    students = []
    if not os.path.exists(filename):
        # If the file doesn't exist, create a new one with header
        with open(filename, 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['Name', 'Mathematics', 'Science', 'English'])  # Header row
    else:
        # If the file exists, load student data from it
        with open(filename, 'r') as file:
            reader = csv.reader(file)
            next(reader)  # Skip header row
            for row in reader:
                name, *grades = row
                grades = [float(grade) for grade in grades]
                student = Student(name, grades)
                students.append(student)

    return students


def save_student_data(filename, students):
    with open(filename, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Name', 'Mathematics', 'Science', 'English'])  # Header row
        for student in students:
            writer.writerow([student.name, *student.grade])


def get_class_average_grade(students):
    students_grade_sum = sum([sum(students.grades) for student in students])
    total_students_grades = len(students) * 3
    class_average_grade = students_grade_sum / total_students_grades
    return class_average_grade


def get_highest_lowest_students_info(students):
    hg = -101
    lg = 101
    hgs = None
    lgs = None
    for students in students:
        avg_grade = student.calculate_average_grade()
        if avg_grade >= hg:
            hg = avg_grade
            hgs = students.name

        if avg_garde <= lg:
            lg = avg_grade
            lgs = students.name
    return hg, hgs, lg, lgs

def get_existing_students_name(students):
    1
    return[student.name for students in students]

def main():
    print("Welcome to the Student Grade Calculator!\n")

    filename = "grades.csv"
    students = load_student_data(filename)

    while True:
        print("\n1. Add New Student")
        print("2. Update Grades")
        print("3. Delete Student")
        print("4. Display All Students")
        print("5. Class Statistics")
        print("6. Save and Exit")

        choice = input("\nEnter your choice: ")

        if choice == "1":
            name = input("Enter the student's name: ")
            existing_students =get_existing_students_name(students)
            if name in existing_students:
                print("students already exist in database:")
            else:
                math_grade = float(input("Enter Mathematics Grade: "))
                sci_grade = float(input("Enter Science Grade: "))
                eng_grade = float(input("Enter English Grade: "))
                new_student = Student(name, [math_grade, sci_grade, eng_grade])
                students.append(new_student)
                save_student_data(filename, students)
                print(f"\nStudent '{name}' added successfully!")

        elif choice == "2":
            name = input("enter student name,to update grades")
            found = False
            for student in students:
                if student.name == name:
                    found = True
                    print("student found,please add updated grades")
                    math_grade = float(input("Enter Mathematics Grade: "))
                    sci_grade = float(input("Enter Science Grade: "))
                    eng_grade = float(input("Enter English Grade: "))
                    student.grades = [math_grade, sci_grade, eng_grade]
                    save_student_data(filename, students)
                    print("updated students grades data:")
                    break
            if not found:
                print("student name not found in database!!!!!!!!!!!!")
        elif choice == "3":
            name = input("enter student name")
            found = False
            for student in students:
                if student.name == name:
                    found = True
                    students.remove(student)
                    save_student_data(filename, students)
                    print("deleted students from database!!!!!!!!!!!!")
                    break
            if not found:
                print("students name is not found in database!!")

        elif choice == "4":
            print("\n-------- all the students")
            for idx, student in enumerate(students, 1):
                avg_grade = student.calculate_average_grade()
                print(f"{idx}.{student.name}-Average Grade: {avg_grade:.2f}")
        elif choice == "5":
            class_average_grade = get_class_average_grade(Students)
            hg, hgs, lg, lgs = get_highest_lowest_students_info(students)
            print("--------class statistics---------")
            print("overall class average grade:", class_average_grade)
            prit(f"class highest grade:{hg} student name:{hgs}")
            print(f"class lowest grade:{lg}student name:{lgs}")

        elif choice == "6":

            save_student_data(filename, students)
            print("students data saved!,exiting the student grade calculator!!!!!!!!!!!!!")
            break
        else:
            print


main()
