# ------------------------------------------------------------------------------------------ #
# Title: Assignment06
# Desc: This assignment demonstrates using functions
# with structured error handling
# Change Log: (Who, When, What)
#   RRoot,1/1/2030,Created Script
#   JGraham,11/16/2026,Created Script
# ------------------------------------------------------------------------------------------ #
import json

# Define the Data Constants
MENU: str = '''
---- Course Registration Program ----
  Select from the following menu:  
    1. Register a Student for a Course.
    2. Show current data.  
    3. Save data to a file.
    4. Exit the program.
----------------------------------------- 
'''
FILE_NAME: str = "Enrollments.json"

# Define the Global Data Variables
student_data: dict = {}  # one row of student data
students: list = []  # a table of student data
file = None  # Holds a reference to an opened file.
menu_choice: str = "" # Holds menu choice input.

#Define the FileProcessor class

class FileProcessor:
    """
    A collection of processing layer functions that work with JSON files.

    Change log (who, when, what)
    JGraham, 11/16/2026, Created Class
    """
    @staticmethod
    def read_data_from_file(FILE_NAME: str, student_data: list):
        """
        Function to read the data from a JSON file.
        Change log (who, when, what)
        JGraham, 11/16/2026, Created Function
        """
        global file
        global students
        try:
            file = open(FILE_NAME, "r")
            students = json.load(file)
        except Exception as e:
            IO.output_error_messages("Error: There was a problem reading from"
                                     " the file. Please check tha the file "
                                     "exists and that it is in "
                                     "a json format.",e)
        finally:
            # Check if a file object exists and is still open
            if file is not None and file.closed == False:
                file.close()
    @staticmethod
    def write_data_to_file(FILE_NAME: str, student_data: list):
        """
        Function to write the data to a JSON file.
        Change log (who, when, what)
        JGraham, 11/16/2026, Created Function
        """
        global file
        global students
        try:
            file = open(FILE_NAME, "w")
            json.dump(students, file, indent=2)
            print("The following data was saved to file!")
            for student in students:
                print(f'Student {student["FirstName"]} '
                      f'{student["LastName"]} is enrolled in {student["CourseName"]}')
        except Exception as e:
            IO.output_error_messages("Error: There was a problem with writing to the file. "
                                     "Please check that the file is not open by another program.",e)
        finally:
            # Check if a file object exists and is still open
            if file is not None and file.closed == False:
                file.close()
    pass

#Define the IO class

class IO:
    """
    A collection of presentation layer functions.

    Change log (who, when, what)
    JGraham, 11/16/2026, Created Class
    """
    @staticmethod
    def output_error_messages(message: str, error: Exception = None):
        """
        Function to present an error message to the user.
        Change log (who, when, what)
        JGraham, 11/17/2026, Created Function
        """
        print(message, end="\n\n")
        if error is not None:
            print("-- Technical Error Message -- ")
            print(error, error.__doc__, type(error), sep='\n')
    @staticmethod
    def output_menu(menu: str):
        """
        Function to present the menu to the user.
        Change log (who, when, what)
        JGraham, 11/16/2026, Created Function
        """
        print(menu)
    @staticmethod
    def input_menu_choice():
        """
        Function to take menu choice input from user.
        Change log (who, when, what)
        JGraham, 11/16/2026, Created Function
        """
        global menu_choice
        menu_choice = input("What would you like to do: ")
    @staticmethod
    def input_student_data(student_data: list):
        """
        Function to input new student data.
        Change log (who, when, what)
        JGraham, 11/16/2026, Created Function
        """
        student_first_name: str = ''
        student_last_name: str = ''
        course_name: str = ''
        try:
            student_first_name = input("Enter the student's first name: ")
            if not student_first_name.isalpha():
                raise ValueError("The first name should not contain numbers.")
            student_last_name = input("Enter the student's last name: ")
            if not student_last_name.isalpha():
                raise ValueError("The last name should not contain numbers.")
            course_name = input("Please enter the name of the course: ")
            student_data = {"FirstName": student_first_name,
                            "LastName": student_last_name,
                            "CourseName": course_name}
            students.append(student_data)
            print(f"You have registered {student_first_name} {student_last_name} for {course_name}.")
        except ValueError as e:
            IO.output_error_messages(str(e), e)
        except Exception as e:
            IO.output_error_messages("Error: There was a problem with your input.")

    @staticmethod
    def output_student_courses(student_data: list):
        """
        Function to display student data.
        Change log (who, when, what)
        JGraham, 11/16/2026, Created Function
        """
        global students
        print("-" * 50)
        for student in students:
            print(f'Student {student["FirstName"]} '
                  f'{student["LastName"]} is enrolled in {student["CourseName"]}')
        print("-" * 50)

    pass

# When the program starts, read the file data into a table
# Extract the data from the file
FileProcessor.read_data_from_file(FILE_NAME, student_data)

# Begin the program loop to present and process data
while True:
    # Present the menu of choices
    IO.output_menu(MENU)
    IO.input_menu_choice()

    # Input user data
    if menu_choice == "1":  # This will not work if it is an integer!
        IO.input_student_data(student_data)
        continue
    # Present the current data
    elif menu_choice == "2":
        IO.output_student_courses(student_data)
        continue
    # Save the data to a file
    elif menu_choice == "3":
        FileProcessor.write_data_to_file(FILE_NAME, student_data)
        continue
    # Stop the loop
    elif menu_choice == "4":
        break  # out of the loop
    else:
        print("Please only choose option 1, 2, or 3")

print("Program Ended")
