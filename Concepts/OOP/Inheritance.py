class Student:

    numberOfStudents = 0

    newAssignments = 1  # class Variable
    marksPerAssignment = 5

    # instance self as first argument
    def __init__(self, firstName, lastName, studentId, remainingAssignments):
        self.firstName = firstName  # self.firstName can be any thing like self.fName
        self.lastName = lastName
        self.studentId = studentId
        self.remainingAssignments = remainingAssignments
        self.email = firstName + '_' + studentId + '@nitc.ac.in'
        Student.numberOfStudents += 1  # increment every time student added

    def fullName(self):
        return ('{} {}'.format(self.firstName, self.lastName))

    def assgn_check(self):
        self.remainingAssignments = int(
            self.remainingAssignments + self.newAssignments)
        return self.remainingAssignments

    def marksToCover(self):
        return (int(self.remainingAssignments * Student.marksPerAssignment))


class Hostel(Student):  # Sub class Section_A inheriting Student Class
    newAssignments = 2

    def __init__(self, firstName, lastName, studentId, remainingAssignments, hostel):
        super().__init__(firstName, lastName, studentId, remainingAssignments)
        # Student.__init__(self, firstName, lastName,
        #                  studentId, remainingAssignments) Same as above line
        self.hostel = hostel


class Teacher(Student):
    def __init__(self, firstName, lastName, studentId, remainingAssignments, students=None):
        super().__init__(firstName, lastName, studentId, remainingAssignments)
        if students is None:
            self.students = []
        else:
            self.students = students

    def add_student(self, student):
        if student not in self.students:
            self.students.append(student)

    def remove_student(self, student):
        if student in self.students:
            self.students.remove(student)

    def print_students(self):
        for student in self.students:
            print('--->', student.fullName())


s_1 = Hostel('Fahadh', 'Fullbuster', 'b190853cs', 2, "B")
s_2 = Hostel('Majidh', 'Master', 'b210853cs', 1, "A")

print(s_1.email, s_1.hostel)
print(s_2.email, s_2.hostel)

# print(help(Hostel))# Helps to get info about class

print(s_1.remainingAssignments)
s_1.assgn_check()
print(s_1.remainingAssignments)

t_1 = Teacher('Fullbuster', 'FF', 'f190853cs', 3, [s_1])

print(t_1.email)
t_1.print_students()
print("Add student")
t_1.add_student(s_2)
t_1.print_students()
print("Remove Student")
t_1.remove_student(s_1)
t_1.print_students()

print("Check Instance")
print(isinstance(t_1, Teacher))  # Checks instance variables of Class
print(isinstance(t_1, Hostel))
print(isinstance(t_1, Student))

print("Check SubClass")
print(issubclass(Teacher, Student))  # Checks subclass variables of Class
print(issubclass(Student, Teacher))
print(issubclass(Teacher, Hostel))
