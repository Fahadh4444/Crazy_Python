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


s_1 = Student('Fahadh', 'Fullbuster', 'b190853cs', 2)
s_2 = Student('Majidh', 'Master', 'b210853cs', 1)

print(Student.newAssignments)
print(s_1.newAssignments)

print(s_2.assgn_check())
print(s_2.marksToCover())

print("newAssignments")
print(Student.newAssignments)
print(s_1.newAssignments)
print(s_2.newAssignments)

print("increment")
Student.newAssignments += 5  # Increases foro every student
print(Student.newAssignments)
print(s_1.newAssignments)
print(s_2.newAssignments)

print("increment")
s_1.newAssignments += 1  # increases for s_1 only
print(Student.newAssignments)
print(s_1.newAssignments)
print(s_2.newAssignments)

print(s_1.__dict__)
print(s_2.__dict__)

print("Number of Students")
print(Student.numberOfStudents)
