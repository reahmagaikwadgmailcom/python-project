students = {}

while True:
    print("\n---- Student Management System ----")
    print("1. Add Student")
    print("2. View Students")
    print("3. Delete Student")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == '1':
        roll = input("Enter Roll Number: ")
        name = input("Enter Student Name: ")
        students[roll] = name
        print("Student added successfully!")

    elif choice == '2':
        if len(students) == 0:
            print("No students found.")
        else:
            print("\nStudent List:")
            for roll, name in students.items():
                print("Roll No:", roll, "| Name:", name)

    elif choice == '3':
        roll = input("Enter Roll Number to delete: ")
        if roll in students:
            del students[roll]
            print("Student deleted successfully!")
        else:
            print("Student not found")

    elif choice == '4':
        print("Exiting program...")
        break

    else:
        print("Invalid choice")
