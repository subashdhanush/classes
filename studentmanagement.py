class Student:
    def __init__(self, name, roll_no, marks):
        self.name = name
        self.roll_no = roll_no
        self.marks = marks

    def display_info(self):
        print(f"🎓 Student Name: {self.name}, Roll No: {self.roll_no}, Marks: {self.marks}")


# Creating student objects
student1 = Student("Alice", 101, 90)
student2 = Student("Bob", 102, 85)

# Displaying student details
student1.display_info()
student2.display_info()
