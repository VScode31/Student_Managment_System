from database import *


def main_menu():
    print("\n===== School Management System =====")
    print("1. Add Student")
    print("2. Remove Student")
    print("3. Update Student")
    print("4. Search Student")
    print("5. Add Teacher")
    print("6. Remove Teacher")
    print("7. Update Teacher")
    print("8. Search Teacher")
    print("9. Add Staff")
    print("10. Remove Staff")
    print("11. Update Staff")
    print("12. Search Staff")
    print("13. Add Subject")
    print("14. Remove Subject")
    print("15. Update Subject")
    print("16. Search Subject")
    print("17. Add Assignment")
    print("18. Remove Assignment")
    print("19. Update Assignment")
    print("20. Search Assignment")
    print("21. Add Class")
    print("22. Remove Class")
    print("23. Update Class")
    print("24. Get All Classes")
    print("25. Get All Teachers")
    print("26. Get All Students")
    print("27. Get All Staff")
    print("28. Get All Subjects")
    print("29. Get All Assignments")
    print("0. Exit")


def main():
    while True:
        main_menu()
        try:
            user_choice = int(input("Enter your choice (0-29): "))
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue

        if user_choice == 0:
            print("Exiting the School Management System. Goodbye!")
            break
        elif user_choice == 1:
            # Get user input for student details
            name = input("Enter student name: ")
            age = int(input("Enter student age: "))
            phone_number = input("Enter student phone number: ")
            date_of_admission = input("Enter date of admission (YYYY-MM-DD): ")

            # Call the add_student() function with the provided arguments
            add_student(name, age, phone_number, date_of_admission)
        elif user_choice == 2:
            # Get user input for student ID to remove
            student_id = int(input("Enter student ID to remove: "))
            remove_student(student_id)
        elif user_choice == 3:
            # Get user input for student details
            student_id = int(input("Enter student ID to update: "))
            new_name = input("Enter new name: ")
            new_age = int(input("Enter new age: "))
            new_phone_number = input("Enter new phone number: ")
            new_date_of_admission = input("Enter new date of admission (YYYY-MM-DD): ")

            # Call the update_student() function with the provided arguments
            update_student(
                student_id, new_name, new_age, new_phone_number, new_date_of_admission
            )
        elif user_choice == 4:
            # Get user input for search criteria and term
            search_by = input("Enter search criteria ('name', 'class', or 'roll_no'): ")
            search_term = input("Enter search term: ")

            # Call the search_student() function with the provided arguments
            search_student(search_term, search_by)
        elif user_choice == 5:
            # Get user input for teacher details
            name = input("Enter teacher name: ")
            qualification = input("Enter teacher qualification: ")
            age = int(input("Enter teacher age: "))
            phone_number = input("Enter teacher phone number: ")
            date_of_joining = input("Enter date of joining (YYYY-MM-DD): ")

            # Call the add_teacher() function with the provided arguments
            add_teacher(name, qualification, age, phone_number, date_of_joining)
        elif user_choice == 6:
            # Get user input for teacher ID to remove
            teacher_id = int(input("Enter teacher ID to remove: "))
            remove_teacher(teacher_id)
        elif user_choice == 7:
            # Get user input for teacher details
            teacher_id = int(input("Enter teacher ID to update: "))
            new_name = input("Enter new name: ")
            new_qualification = input("Enter new qualification: ")
            new_age = int(input("Enter new age: "))
            new_phone_number = input("Enter new phone number: ")
            new_date_of_joining = input("Enter new date of joining (YYYY-MM-DD): ")

            # Call the update_teacher() function with the provided arguments
            update_teacher(
                teacher_id,
                new_name,
                new_qualification,
                new_age,
                new_phone_number,
                new_date_of_joining,
            )
        elif user_choice == 8:
            # Get user input for search criteria and term
            search_by = input("Enter search criteria ('name' or 'qualification'): ")
            search_term = input("Enter search term: ")

            # Call the search_teacher() function with the provided arguments
            search_teacher(search_term, search_by)
        elif user_choice == 9:
            # Get user input for staff details
            name = input("Enter staff member name: ")
            qualification = input("Enter staff member qualification: ")
            age = int(input("Enter staff member age: "))
            phone_number = input("Enter staff member phone number: ")
            role = input("Enter staff member role: ")
            date_of_joining = input("Enter date of joining (YYYY-MM-DD): ")

            # Call the add_staff() function with the provided arguments
            add_staff(name, qualification, age, phone_number, role, date_of_joining)
        elif user_choice == 10:
            # Get user input for staff ID to remove
            staff_id = int(input("Enter staff member ID to remove: "))
            remove_staff(staff_id)
        elif user_choice == 11:
            # Get user input for staff details
            staff_id = int(input("Enter staff member ID to update: "))
            new_name = input("Enter new name: ")
            new_qualification = input("Enter new qualification: ")
            new_age = int(input("Enter new age: "))
            new_phone_number = input("Enter new phone number: ")
            new_role = input("Enter new role: ")
            new_date_of_joining = input("Enter new date of joining (YYYY-MM-DD): ")

            # Call the update_staff() function with the provided arguments
            update_staff(
                staff_id,
                new_name,
                new_qualification,
                new_age,
                new_phone_number,
                new_role,
                new_date_of_joining,
            )
        elif user_choice == 12:
            # Get user input for search criteria and term
            search_by = input(
                "Enter search criteria ('name', 'role', or 'qualification'): "
            )
            search_term = input("Enter search term: ")

            # Call the search_staff() function with the provided arguments
            search_staff(search_term, search_by)
        elif user_choice == 13:
            # Get user input for subject details
            name = input("Enter subject name: ")
            code = input("Enter subject code: ")
            teacher_id = int(input("Enter teacher ID for the subject: "))

            # Call the add_subject() function with the provided arguments
            add_subject(name, code, teacher_id)
        elif user_choice == 14:
            # Get user input for subject ID to remove
            subject_id = int(input("Enter subject ID to remove: "))
            remove_subject(subject_id)
        elif user_choice == 15:
            # Get user input for subject details
            subject_id = int(input("Enter subject ID to update: "))
            new_name = input("Enter new name: ")
            new_code = input("Enter new code: ")
            new_teacher_id = int(input("Enter new teacher ID: "))

            # Call the update_subject() function with the provided arguments
            update_subject(subject_id, new_name, new_code, new_teacher_id)
        elif user_choice == 16:
            # Get user input for search criteria and term
            search_by = input("Enter search criteria ('name' or 'code'): ")
            search_term = input("Enter search term: ")

            # Call the search_subject() function with the provided arguments
            search_subject(search_term, search_by)
        elif user_choice == 17:
            # Get user input for assignment details
            name = input("Enter assignment name: ")
            subject_id = int(input("Enter subject ID for the assignment: "))
            due_date = input("Enter due date (YYYY-MM-DD): ")

            # Call the add_assignment() function with the provided arguments
            add_assignment(name, subject_id, due_date)
        elif user_choice == 18:
            # Get user input for assignment ID to remove
            assignment_id = int(input("Enter assignment ID to remove: "))
            remove_assignment(assignment_id)
        elif user_choice == 19:
            # Get user input for assignment details
            assignment_id = int(input("Enter assignment ID to update: "))
            new_name = input("Enter new name: ")
            new_subject_id = int(input("Enter new subject ID: "))
            new_due_date = input("Enter new due date (YYYY-MM-DD): ")

            # Call the update_assignment() function with the provided arguments
            update_assignment(assignment_id, new_name, new_subject_id, new_due_date)
        elif user_choice == 20:
            # Get user input for search criteria and term
            search_by = input("Enter search criteria ('name' or 'subject'): ")
            search_term = input("Enter search term: ")

            # Call the search_assignment() function with the provided arguments
            search_assignment(search_term, search_by)
        elif user_choice == 21:
            # Get user input for class details
            name = input("Enter class name: ")
            teacher_id = int(input("Enter teacher ID for the class: "))

            # Call the add_class() function with the provided arguments
            add_class(name, teacher_id)
        elif user_choice == 22:
            # Get user input for class ID to remove
            class_id = int(input("Enter class ID to remove: "))
            remove_class(class_id)
        elif user_choice == 23:
            # Get user input for class details
            class_id = int(input("Enter class ID to update: "))
            new_name = input("Enter new name: ")
            new_teacher_id = int(input("Enter new teacher ID: "))

            # Call the update_class() function with the provided arguments
            update_class(class_id, new_name, new_teacher_id)
        elif user_choice == 24:
            # Call the get_all_classes() function to retrieve all classes
            get_all_classes()
        elif user_choice == 25:
            # Call the get_all_teachers() function to retrieve all teachers
            get_all_teachers()
        elif user_choice == 26:
            # Call the get_all_students() function to retrieve all students
            get_all_students()
        elif user_choice == 27:
            # Call the get_all_staff() function to retrieve all staff members
            get_all_staff()
        elif user_choice == 28:
            # Call the get_all_subjects() function to retrieve all subjects
            get_all_subjects()
        elif user_choice == 29:
            # Call the get_all_assignments() function to retrieve all assignments
            get_all_assignments()
        else:
            print("Invalid choice. Please enter a number between 0 and 29.")


if __name__ == "__main__":
    main()
