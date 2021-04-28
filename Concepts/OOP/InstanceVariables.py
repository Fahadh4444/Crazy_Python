class Employee:
    pass  # pass keyword tells python to skip corresponding class


emp_1 = Employee()
emp_2 = Employee()
# Above both have differnt addresses
print(emp_1)
print(emp_2)


class Student:
    def __init__(self, firstName, lastName, studentId):  # instance self as first argument
        self.firstName = firstName  # self.firstName can be any thing like self.fName
        self.lastName = lastName
        self.studentId = studentId
        self.email = firstName + '_' + studentId + '@nitc.ac.in'

    def fullName(self):
        return ('{} {}'.format(self.firstName, self.lastName))


s_1 = Student('Fahadh', 'Fullbuster', 'b190853cs')  # instance variables
s_2 = Student('Majidh', 'Master', 'b210853cs')
print(s_1.email, s_1.fullName)  # Printd address
print(s_2.email, s_2.fullName())  # prints fullname

print(s_2.fullName())
print(Student.fullName(s_2))  # argument required
# Above Both are Same
# print(Student.fullName())#ERROR
