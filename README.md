# Student Record System

## 1. Project Overview

The Student Record System is a Python application developed for the Object-Oriented Programming 1 (PROG211) course. It demonstrates how object-oriented programming can be used to manage student records and course information.

## 2. Problem Statement

Managing student information manually can be time-consuming. This project demonstrates a simple way to store, add, and display student records using Python.

## 3. Project Objectives

- To demonstrate object-oriented programming concepts.
- To create and use classes and objects.
- To store multiple student records using a list.
- To add and display student information.
- To demonstrate interaction between Student and Course objects.

## 4. Technologies Used

- Programming Language: Python
- Code Editor: Visual Studio Code

## 5. Classes and Methods

### Student Class

The Student class stores the student's ID, name, and age.

Methods:
- `display_info()` displays student information.
- `display_course()` displays information about a course associated with the student.
- `display_total_students()` displays the number of student records.

### Course Class

The Course class stores the course code and course name.

Method:
- `display_course()` displays course information.

## 6. Data Structure

The program uses a Python list named `students` to store multiple Student objects.

The `add_student()` function adds a student to the list, while `display_students()` displays the student records.

## 7. How to Run the Program

1. Install Python.
2. Open the project folder in Visual Studio Code.
3. Open the terminal.
4. Run the following command:

   `py main.py`

5. Follow the prompts to enter the student's ID, name, and age.

## 8. Digital Public Goods Principles

### Open Source
The project can be shared through a public GitHub repository so others can study, use, and improve the code. An appropriate open-source licence should be included.

### Inclusive and Accessible Design
The program uses simple text prompts and clear messages to help users interact with it.

### Privacy and Data Protection
The program uses basic student details for demonstration. Real student information should be protected, and sensitive personal data should not be exposed.

### Modularity and Reusability
The program separates responsibilities into classes and functions, making the code easier to understand, maintain, and extend.

## 9. Limitations

The program stores records in memory. Student records are not automatically saved to a permanent database or file, so they are lost when the program closes.

## 10. Future Improvements

- Save student records to a file or database.
- Allow users to search for students.
- Allow users to update or delete records.
- Add stronger input validation.

## 11. Conclusion

The Student Record System demonstrates fundamental Python object-oriented programming concepts, including classes, objects, methods, and data structures. It provides a foundation for developing more advanced student management applications.