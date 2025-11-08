class StudentDatabase:
    __student_list = []
        
    @classmethod
    def add_student(self,student):
        self.__student_list.append(student)

    @classmethod
    def get_all_students(self):
        return self.__student_list
    
    @classmethod
    def find_stu_by_id(self, student_id):
        for student in self.__student_list:
            if student.get_student_id() == student_id:
                return student
        return None    
        


class Student:
    def __init__(self, name, student_id, department, is_enrolled = False):
        self.__name = name
        self.__student_id = student_id
        self.__dept = department
        self.__enroll = is_enrolled
        StudentDatabase.add_student(self)

    def get_student_id(self):
        return self.__student_id
    
    def enroll_student(self):
        if self.__enroll:
            raise Exception(f'{self.__name} is already enrolled\n')
        self.__enroll = True
        print(f'{self.__name} is successfully enrolled\n')

    def drop_student(self):
        if  not self.__enroll:
            raise Exception(f'{self.__name} is not enrolled yet\n')
        self.__enroll = False
        print(f'{self.__name} is dropped out\n')
    
    def view_student_info(self):
        status = "Enrolled" if self.__enroll else "Not enrolled"
        print(f'Name: {self.__name}\nID: {self.__student_id}\nDept: {self.__dept}\nStatus:{status}\n\n')




jamshed = Student('Jam', 23, 'CSE', True)
mumir = Student('Mumir', 22, 'CSE', False)
Kamrul = Student('Kamrul', 18, 'Science',True)

while True:
    print("\t---------Student Management System---------")
    print("1. View All Students")
    print("2. Enroll Student")
    print("3. Drop Student")
    print("4. Exit")

    choice = input("Enter your Choice(1-4): ")

    if choice == '1':
        print("\n----All Students----")
        all_students = StudentDatabase.get_all_students()
        if not all_students:
            print('No students in the database')
        else:
            for stu in all_students:
                stu.view_student_info()
    
    elif choice == '2':
        try:
            stu_id = int(input("Enter student id to enroll: "))
            student = StudentDatabase.find_stu_by_id(stu_id)
            if student:
               student.enroll_student()
            else:
                print('Invalid Student id')
        except:
            print("Please enter a valid student ID")

    
    elif choice == '3':
        try:
            stu_id = int(input("Enter student id to drop: "))
            student = StudentDatabase.find_stu_by_id(stu_id)
            if student:
               student.drop_student()
            else:
                print('Invalid Student id')
        except:
            print("Please enter a valid student ID")

    elif choice == '4':
        print("Exist")
        break
    else:
        print("Invalid choice. Please enter (1-4)")


