student = {}

print("\n-----STUDENT MANAGER APP-----")
print("1. Add student")
print("2. Check marks")
print("3. Edit")
print("4. Delete")
print("5. View all students")
print("6. Exit")

while True :

    x = int(input("Enter choice (1- 6) : "))

    if x == 1 :
        name = input("Enter the name of the student to add : ")
        if name in student :
            print(f"{name} already exist")
        else:
            marks = float(input("Enter marks :"))
            student[name] = marks
            print("Successfully added.")

    elif x == 2:
        name = input("Enter the name of the student to check marks : ")
        if name in student :
            print(f"{name} : {student[name]}")
        else:
            print("Student not found")

    elif x == 3:
        name = input("Enter the name of the student to edit : ")
        if name in student :
            z = input("What you want to edit student name or marks (enter N for name & M for marks) ? ")
            if z == 'N' :
                nname = input("New name : ")
                student[nname] = student.pop(name)
                print("Name updated")
            elif z == "M" :
                nmarks = float(input("New marks : "))
                student[name] = nmarks
                print("Marks updated ")
            else:
                print("Enter 'N' or 'M'")
        else:
            print("Student not found")

    elif x == 4:
        name = input("Enter the name of the student to delete : ")
        if name in student :
            del student[name]
            print("Successfully deleted name")
        else:
            print("Student not found")

    elif x == 5:
        if not student:
            print("Student list is empty ")
        else:
            print("---- ALL STUDENTS ----")
            for name, marks in student.items():
                print(f"{name} : {student[name]}")


    elif x == 6:
        print("Exiting the app . ")
        break
    else:
        print("Choose only between 1 to 6")


            
    
    
