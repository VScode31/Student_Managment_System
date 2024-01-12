# database.py
import mysql.connector
from mysql.connector import Error


def get_connection():
    """Establish a database connection."""
    try:
        connection = mysql.connector.connect(
            host="127.0.0.1",
            user="root",
            password="123sumit",
            database="School_Management",
        )
        return connection
    except Error as e:
        print(f"Error: {e}")
        return None


def create_database():
    """Create the School_Management database."""
    try:
        connection = get_connection()
        if connection:
            cursor = connection.cursor()
            cursor.execute("CREATE DATABASE IF NOT EXISTS School_Management;")
            print("Database 'School_Management' created successfully.")
    finally:
        if connection and connection.is_connected():
            cursor.close()
            connection.close()


def create_student_table():
    """Create the Student table."""
    try:
        connection = get_connection()
        if connection:
            cursor = connection.cursor()
            cursor.execute(
                """
                CREATE TABLE IF NOT EXISTS Student (
                    Student_ID INT AUTO_INCREMENT PRIMARY KEY,
                    Name VARCHAR(255) NOT NULL,
                    Age INT,
                    Phone_Number VARCHAR(15),
                    Date_of_Admission DATE,
                    Date_of_Removal DATE
                );
                """
            )
            print("Table 'Student' created successfully.")
    finally:
        if connection and connection.is_connected():
            cursor.close()
            connection.close()


def create_teacher_table():
    """Create the Teacher table."""
    try:
        connection = get_connection()
        if connection:
            cursor = connection.cursor()
            cursor.execute(
                """
                CREATE TABLE IF NOT EXISTS Teacher (
                    Teacher_ID INT AUTO_INCREMENT PRIMARY KEY,
                    Name VARCHAR(255) NOT NULL,
                    Qualification VARCHAR(255),
                    Age INT,
                    Phone_Number VARCHAR(15),
                    Date_of_Joining DATE,
                    Date_of_Exit DATE
                );
                """
            )
            print("Table 'Teacher' created successfully.")
    finally:
        if connection and connection.is_connected():
            cursor.close()
            connection.close()


def create_staff_table():
    """Create the Staff table."""
    try:
        connection = get_connection()
        if connection:
            cursor = connection.cursor()
            cursor.execute(
                """
                CREATE TABLE IF NOT EXISTS Staff (
                    Staff_ID INT AUTO_INCREMENT PRIMARY KEY,
                    Name VARCHAR(255) NOT NULL,
                    Qualification VARCHAR(255),
                    Age INT,
                    Phone_Number VARCHAR(15),
                    Role VARCHAR(50),
                    Date_of_Joining DATE,
                    Date_of_Exit DATE
                );
                """
            )
            print("Table 'Staff' created successfully.")
    finally:
        if connection and connection.is_connected():
            cursor.close()
            connection.close()


def create_class_table():
    """Create the Class table."""
    try:
        connection = get_connection()
        if connection:
            cursor = connection.cursor()
            cursor.execute(
                """
                CREATE TABLE IF NOT EXISTS Class (
                    Class_ID INT AUTO_INCREMENT PRIMARY KEY,
                    Class_Name VARCHAR(50) NOT NULL,
                    Class_Description VARCHAR(255),
                    Class_Teacher_ID INT,
                    FOREIGN KEY (Class_Teacher_ID) REFERENCES Teacher(Teacher_ID)
                );
                """
            )
            print("Table 'Class' created successfully.")
    finally:
        if connection and connection.is_connected():
            cursor.close()
            connection.close()


def create_subject_table():
    """Create the Subject table."""
    try:
        connection = get_connection()
        if connection:
            cursor = connection.cursor()
            cursor.execute(
                """
                CREATE TABLE IF NOT EXISTS Subject (
                    Subject_ID INT AUTO_INCREMENT PRIMARY KEY,
                    Subject_Name VARCHAR(50) NOT NULL,
                    Subject_Description VARCHAR(255)
                );
                """
            )
            print("Table 'Subject' created successfully.")
    finally:
        if connection and connection.is_connected():
            cursor.close()
            connection.close()


def create_assignment_table():
    """Create the Assignment table."""
    try:
        connection = get_connection()
        if connection:
            cursor = connection.cursor()
            cursor.execute(
                """
                CREATE TABLE IF NOT EXISTS Assignment (
                    Assignment_ID INT AUTO_INCREMENT PRIMARY KEY,
                    Assignment_Name VARCHAR(100) NOT NULL,
                    Assignment_Description VARCHAR(255),
                    Subject_ID INT,
                    FOREIGN KEY (Subject_ID) REFERENCES Subject(Subject_ID)
                );
                """
            )
            print("Table 'Assignment' created successfully.")
    finally:
        if connection and connection.is_connected():
            cursor.close()
            connection.close()


def add_student(name, age, phone_number, date_of_admission):
    """Add a new student to the Student table."""
    try:
        connection = get_connection()
        if connection:
            cursor = connection.cursor()
            query = """
                INSERT INTO Student (Name, Age, Phone_Number, Date_of_Admission)
                VALUES (%s, %s, %s, %s);
            """
            data = (name, age, phone_number, date_of_admission)
            cursor.execute(query, data)
            connection.commit()
            print(f"Student '{name}' added successfully.")
    finally:
        if connection and connection.is_connected():
            cursor.close()
            connection.close()


def remove_student(student_id):
    """Remove a student from the Student table."""
    try:
        connection = get_connection()
        if connection:
            cursor = connection.cursor()
            query = "DELETE FROM Student WHERE Student_ID = %s;"
            data = (student_id,)
            cursor.execute(query, data)
            connection.commit()
            print(f"Student with ID {student_id} removed successfully.")
    finally:
        if connection and connection.is_connected():
            cursor.close()
            connection.close()


def update_student(
    student_id, new_name, new_age, new_phone_number, new_date_of_admission
):
    """Update student information in the Student table."""
    try:
        connection = get_connection()
        if connection:
            cursor = connection.cursor()
            query = """
                UPDATE Student
                SET Name = %s, Age = %s, Phone_Number = %s, Date_of_Admission = %s
                WHERE Student_ID = %s;
            """
            data = (
                new_name,
                new_age,
                new_phone_number,
                new_date_of_admission,
                student_id,
            )
            cursor.execute(query, data)
            connection.commit()
            print(f"Student with ID {student_id} updated successfully.")
    finally:
        if connection and connection.is_connected():
            cursor.close()
            connection.close()


def search_student(search_term, search_by="name"):
    """Search for a student based on name, class, or roll number."""
    try:
        connection = get_connection()
        if connection:
            cursor = connection.cursor()

            if search_by == "name":
                query = "SELECT * FROM Student WHERE Name LIKE %s;"
                data = (f"%{search_term}%",)
            elif search_by == "class":
                query = """
                    SELECT S.*
                    FROM Student S
                    INNER JOIN Student_Class_Assignment A ON S.Student_ID = A.Student_ID
                    INNER JOIN Class C ON A.Class_ID = C.Class_ID
                    WHERE C.Class_Name LIKE %s;
                """
                data = (f"%{search_term}%",)
            elif search_by == "roll_no":
                query = """
                    SELECT * FROM Student WHERE Student_ID = %s;
                """
                data = (int(search_term),)
            else:
                print("Invalid search criteria. Use 'name', 'class', or 'roll_no'.")
                return

            cursor.execute(query, data)
            result = cursor.fetchall()

            if result:
                print("Search results for Students:")
                for row in result:
                    print(row)
            else:
                print("No matching records found for Students.")

    finally:
        if connection and connection.is_connected():
            cursor.close()
            connection.close()


def add_teacher(name, qualification, age, phone_number, date_of_joining):
    """Add a new teacher to the Teacher table."""
    try:
        connection = get_connection()
        if connection:
            cursor = connection.cursor()
            query = """
                INSERT INTO Teacher (Name, Qualification, Age, Phone_Number, Date_of_Joining)
                VALUES (%s, %s, %s, %s, %s);
            """
            data = (name, qualification, age, phone_number, date_of_joining)
            cursor.execute(query, data)
            connection.commit()
            print(f"Teacher '{name}' added successfully.")
    finally:
        if connection and connection.is_connected():
            cursor.close()
            connection.close()


def remove_teacher(teacher_id):
    """Remove a teacher from the Teacher table."""
    try:
        connection = get_connection()
        if connection:
            cursor = connection.cursor()
            query = "DELETE FROM Teacher WHERE Teacher_ID = %s;"
            data = (teacher_id,)
            cursor.execute(query, data)
            connection.commit()
            print(f"Teacher with ID {teacher_id} removed successfully.")
    finally:
        if connection and connection.is_connected():
            cursor.close()
            connection.close()


def update_teacher(
    teacher_id,
    new_name,
    new_qualification,
    new_age,
    new_phone_number,
    new_date_of_joining,
):
    """Update teacher information in the Teacher table."""
    try:
        connection = get_connection()
        if connection:
            cursor = connection.cursor()
            query = """
                UPDATE Teacher
                SET Name = %s, Qualification = %s, Age = %s, Phone_Number = %s, Date_of_Joining = %s
                WHERE Teacher_ID = %s;
            """
            data = (
                new_name,
                new_qualification,
                new_age,
                new_phone_number,
                new_date_of_joining,
                teacher_id,
            )
            cursor.execute(query, data)
            connection.commit()
            print(f"Teacher with ID {teacher_id} updated successfully.")
    finally:
        if connection and connection.is_connected():
            cursor.close()
            connection.close()


def search_teacher(search_term, search_by="name"):
    """Search for a teacher based on name or qualification."""
    try:
        connection = get_connection()
        if connection:
            cursor = connection.cursor()

            if search_by == "name":
                query = "SELECT * FROM Teacher WHERE Name LIKE %s;"
                data = (f"%{search_term}%",)
            elif search_by == "qualification":
                query = "SELECT * FROM Teacher WHERE Qualification LIKE %s;"
                data = (f"%{search_term}%",)
            else:
                print("Invalid search criteria. Use 'name' or 'qualification'.")
                return

            cursor.execute(query, data)
            result = cursor.fetchall()

            if result:
                print("Search results for Teachers:")
                for row in result:
                    print(row)
            else:
                print("No matching records found for Teachers.")

    finally:
        if connection and connection.is_connected():
            cursor.close()
            connection.close()


def add_staff(name, qualification, age, phone_number, role, date_of_joining):
    """Add a new staff member to the Staff table."""
    try:
        connection = get_connection()
        if connection:
            cursor = connection.cursor()
            query = """
                INSERT INTO Staff (Name, Qualification, Age, Phone_Number, Role, Date_of_Joining)
                VALUES (%s, %s, %s, %s, %s, %s);
            """
            data = (name, qualification, age, phone_number, role, date_of_joining)
            cursor.execute(query, data)
            connection.commit()
            print(f"Staff member '{name}' added successfully.")
    finally:
        if connection and connection.is_connected():
            cursor.close()
            connection.close()


def remove_staff(staff_id):
    """Remove a staff member from the Staff table."""
    try:
        connection = get_connection()
        if connection:
            cursor = connection.cursor()
            query = "DELETE FROM Staff WHERE Staff_ID = %s;"
            data = (staff_id,)
            cursor.execute(query, data)
            connection.commit()
            print(f"Staff member with ID {staff_id} removed successfully.")
    finally:
        if connection and connection.is_connected():
            cursor.close()
            connection.close()


def update_staff(
    staff_id,
    new_name,
    new_qualification,
    new_age,
    new_phone_number,
    new_role,
    new_date_of_joining,
):
    """Update staff member information in the Staff table."""
    try:
        connection = get_connection()
        if connection:
            cursor = connection.cursor()
            query = """
                UPDATE Staff
                SET Name = %s, Qualification = %s, Age = %s, Phone_Number = %s, Role = %s, Date_of_Joining = %s
                WHERE Staff_ID = %s;
            """
            data = (
                new_name,
                new_qualification,
                new_age,
                new_phone_number,
                new_role,
                new_date_of_joining,
                staff_id,
            )
            cursor.execute(query, data)
            connection.commit()
            print(f"Staff member with ID {staff_id} updated successfully.")
    finally:
        if connection and connection.is_connected():
            cursor.close()
            connection.close()


def search_staff(search_term, search_by="name"):
    """Search for a staff member based on name or role."""
    try:
        connection = get_connection()
        if connection:
            cursor = connection.cursor()

            if search_by == "name":
                query = "SELECT * FROM Staff WHERE Name LIKE %s;"
                data = (f"%{search_term}%",)
            elif search_by == "role":
                query = "SELECT * FROM Staff WHERE Role LIKE %s;"
                data = (f"%{search_term}%",)
            else:
                print("Invalid search criteria. Use 'name' or 'role'.")
                return

            cursor.execute(query, data)
            result = cursor.fetchall()

            if result:
                print("Search results for Staff:")
                for row in result:
                    print(row)
            else:
                print("No matching records found for Staff.")

    finally:
        if connection and connection.is_connected():
            cursor.close()
            connection.close()


def search_subject(search_term, search_by="name"):
    """Search for a subject based on name or description."""
    try:
        connection = get_connection()
        if connection:
            cursor = connection.cursor()

            if search_by == "name":
                query = "SELECT * FROM Subject WHERE Subject_Name LIKE %s;"
                data = (f"%{search_term}%",)
            elif search_by == "description":
                query = "SELECT * FROM Subject WHERE Subject_Description LIKE %s;"
                data = (f"%{search_term}%",)
            else:
                print("Invalid search criteria. Use 'name' or 'description'.")
                return

            cursor.execute(query, data)
            result = cursor.fetchall()

            if result:
                print("Search results for Subjects:")
                for row in result:
                    print(row)
            else:
                print("No matching records found for Subjects.")

    finally:
        if connection and connection.is_connected():
            cursor.close()
            connection.close()


def add_subject(subject_name, subject_description):
    """Add a new subject to the Subject table."""
    try:
        connection = get_connection()
        if connection:
            cursor = connection.cursor()
            query = """
                INSERT INTO Subject (Subject_Name, Subject_Description)
                VALUES (%s, %s);
            """
            data = (subject_name, subject_description)
            cursor.execute(query, data)
            connection.commit()
            print(f"Subject '{subject_name}' added successfully.")
    finally:
        if connection and connection.is_connected():
            cursor.close()
            connection.close()


def remove_subject(subject_id):
    """Remove a subject from the Subject table."""
    try:
        connection = get_connection()
        if connection:
            cursor = connection.cursor()
            query = "DELETE FROM Subject WHERE Subject_ID = %s;"
            data = (subject_id,)
            cursor.execute(query, data)
            connection.commit()
            print(f"Subject with ID {subject_id} removed successfully.")
    finally:
        if connection and connection.is_connected():
            cursor.close()
            connection.close()


def update_subject(subject_id, new_name, new_description):
    """Update subject information in the Subject table."""
    try:
        connection = get_connection()
        if connection:
            cursor = connection.cursor()
            query = """
                UPDATE Subject
                SET Subject_Name = %s, Subject_Description = %s
                WHERE Subject_ID = %s;
            """
            data = (new_name, new_description, subject_id)
            cursor.execute(query, data)
            connection.commit()
            print(f"Subject with ID {subject_id} updated successfully.")
    finally:
        if connection and connection.is_connected():
            cursor.close()
            connection.close()


def search_assignment(search_term, search_by="name"):
    """Search for an assignment based on name or description."""
    try:
        connection = get_connection()
        if connection:
            cursor = connection.cursor()

            if search_by == "name":
                query = "SELECT * FROM Assignment WHERE Assignment_Name LIKE %s;"
                data = (f"%{search_term}%",)
            elif search_by == "description":
                query = "SELECT * FROM Assignment WHERE Assignment_Description LIKE %s;"
                data = (f"%{search_term}%",)
            else:
                print("Invalid search criteria. Use 'name' or 'description'.")
                return

            cursor.execute(query, data)
            result = cursor.fetchall()

            if result:
                print("Search results for Assignments:")
                for row in result:
                    print(row)
            else:
                print("No matching records found for Assignments.")

    finally:
        if connection and connection.is_connected():
            cursor.close()
            connection.close()


def add_assignment(assignment_name, assignment_description, subject_id):
    """Add a new assignment to the Assignment table."""
    try:
        connection = get_connection()
        if connection:
            cursor = connection.cursor()
            query = """
                INSERT INTO Assignment (Assignment_Name, Assignment_Description, Subject_ID)
                VALUES (%s, %s, %s);
            """
            data = (assignment_name, assignment_description, subject_id)
            cursor.execute(query, data)
            connection.commit()
            print(f"Assignment '{assignment_name}' added successfully.")
    finally:
        if connection and connection.is_connected():
            cursor.close()
            connection.close()


def remove_assignment(assignment_id):
    """Remove an assignment from the Assignment table."""
    try:
        connection = get_connection()
        if connection:
            cursor = connection.cursor()
            query = "DELETE FROM Assignment WHERE Assignment_ID = %s;"
            data = (assignment_id,)
            cursor.execute(query, data)
            connection.commit()
            print(f"Assignment with ID {assignment_id} removed successfully.")
    finally:
        if connection and connection.is_connected():
            cursor.close()
            connection.close()


def update_assignment(assignment_id, new_name, new_description):
    """Update assignment information in the Assignment table."""
    try:
        connection = get_connection()
        if connection:
            cursor = connection.cursor()
            query = """
                UPDATE Assignment
                SET Assignment_Name = %s, Assignment_Description = %s
                WHERE Assignment_ID = %s;
            """
            data = (new_name, new_description, assignment_id)
            cursor.execute(query, data)
            connection.commit()
            print(f"Assignment with ID {assignment_id} updated successfully.")
    finally:
        if connection and connection.is_connected():
            cursor.close()
            connection.close()


def assign_subject_to_class(subject_id, class_id):
    """Assign a subject to a class in the Assignment table."""
    try:
        connection = get_connection()
        if connection:
            cursor = connection.cursor()
            query = """
                INSERT INTO Subject_Class_Assignment (Subject_ID, Class_ID)
                VALUES (%s, %s);
            """
            data = (subject_id, class_id)
            cursor.execute(query, data)
            connection.commit()
            print(
                f"Subject with ID {subject_id} assigned to Class with ID {class_id} successfully."
            )
    finally:
        if connection and connection.is_connected():
            cursor.close()
            connection.close()


def unassign_subject_from_class(subject_id, class_id):
    """Unassign a subject from a class in the Assignment table."""
    try:
        connection = get_connection()
        if connection:
            cursor = connection.cursor()
            query = """
                DELETE FROM Subject_Class_Assignment
                WHERE Subject_ID = %s AND Class_ID = %s;
            """
            data = (subject_id, class_id)
            cursor.execute(query, data)
            connection.commit()
            print(
                f"Subject with ID {subject_id} unassigned from Class with ID {class_id} successfully."
            )
    finally:
        if connection and connection.is_connected():
            cursor.close()
            connection.close()


def search_class(search_term, search_by="name"):
    """Search for a class based on name or description."""
    try:
        connection = get_connection()
        if connection:
            cursor = connection.cursor()

            if search_by == "name":
                query = "SELECT * FROM Class WHERE Class_Name LIKE %s;"
                data = (f"%{search_term}%",)
            else:
                print("Invalid search criteria. Use 'name'.")
                return

            cursor.execute(query, data)
            result = cursor.fetchall()

            if result:
                print("Search results for Classes:")
                for row in result:
                    print(row)
            else:
                print("No matching records found for Classes.")

    finally:
        if connection and connection.is_connected():
            cursor.close()
            connection.close()


def add_class(class_name, class_description, class_teacher_id):
    """Add a new class to the Class table."""
    try:
        connection = get_connection()
        if connection:
            cursor = connection.cursor()
            query = """
                INSERT INTO Class (Class_Name, Class_Description, Class_Teacher_ID)
                VALUES (%s, %s, %s);
            """
            data = (class_name, class_description, class_teacher_id)
            cursor.execute(query, data)
            connection.commit()
            print(f"Class '{class_name}' added successfully.")
    finally:
        if connection and connection.is_connected():
            cursor.close()
            connection.close()


def remove_class(class_id):
    """Remove a class from the Class table."""
    try:
        connection = get_connection()
        if connection:
            cursor = connection.cursor()
            query = "DELETE FROM Class WHERE Class_ID = %s;"
            data = (class_id,)
            cursor.execute(query, data)
            connection.commit()
            print(f"Class with ID {class_id} removed successfully.")
    finally:
        if connection and connection.is_connected():
            cursor.close()
            connection.close()


def update_class(class_id, new_name, new_description, new_teacher_id):
    """Update class information in the Class table."""
    try:
        connection = get_connection()
        if connection:
            cursor = connection.cursor()
            query = """
                UPDATE Class
                SET Class_Name = %s, Class_Description = %s, Class_Teacher_ID = %s
                WHERE Class_ID = %s;
            """
            data = (new_name, new_description, new_teacher_id, class_id)
            cursor.execute(query, data)
            connection.commit()
            print(f"Class with ID {class_id} updated successfully.")
    finally:
        if connection and connection.is_connected():
            cursor.close()
            connection.close()


def get_all_classes():
    """Get all classes from the Class table."""
    try:
        connection = get_connection()
        if connection:
            cursor = connection.cursor()
            query = "SELECT * FROM Class;"
            cursor.execute(query)
            result = cursor.fetchall()

            if result:
                print("All Classes:")
                for row in result:
                    print(row)
            else:
                print("No records found for Classes.")
    finally:
        if connection and connection.is_connected():
            cursor.close()
            connection.close()


def get_all_teachers():
    """Get all teachers from the Teacher table."""
    try:
        connection = get_connection()
        if connection:
            cursor = connection.cursor()
            query = "SELECT * FROM Teacher;"
            cursor.execute(query)
            result = cursor.fetchall()

            if result:
                print("All Teachers:")
                for row in result:
                    print(row)
            else:
                print("No records found for Teachers.")
    finally:
        if connection and connection.is_connected():
            cursor.close()
            connection.close()


def get_all_students():
    """Get all students from the Student table."""
    try:
        connection = get_connection()
        if connection:
            cursor = connection.cursor()
            query = "SELECT * FROM Student;"
            cursor.execute(query)
            result = cursor.fetchall()

            if result:
                print("All Students:")
                for row in result:
                    print(row)
            else:
                print("No records found for Students.")
    finally:
        if connection and connection.is_connected():
            cursor.close()
            connection.close()


def get_all_staff():
    """Get all staff members from the Staff table."""
    try:
        connection = get_connection()
        if connection:
            cursor = connection.cursor()
            query = "SELECT * FROM Staff;"
            cursor.execute(query)
            result = cursor.fetchall()

            if result:
                print("All Staff Members:")
                for row in result:
                    print(row)
            else:
                print("No records found for Staff.")
    finally:
        if connection and connection.is_connected():
            cursor.close()
            connection.close()


def get_all_subjects():
    """Get all subjects from the Subject table."""
    try:
        connection = get_connection()
        if connection:
            cursor = connection.cursor()
            query = "SELECT * FROM Subject;"
            cursor.execute(query)
            result = cursor.fetchall()

            if result:
                print("All Subjects:")
                for row in result:
                    print(row)
            else:
                print("No records found for Subjects.")
    finally:
        if connection and connection.is_connected():
            cursor.close()
            connection.close()


def get_all_assignments():
    """Get all assignments from the Assignment table."""
    try:
        connection = get_connection()
        if connection:
            cursor = connection.cursor()
            query = "SELECT * FROM Assignment;"
            cursor.execute(query)
            result = cursor.fetchall()

            if result:
                print("All Assignments:")
                for row in result:
                    print(row)
            else:
                print("No records found for Assignments.")
    finally:
        if connection and connection.is_connected():
            cursor.close()
            connection.close()
