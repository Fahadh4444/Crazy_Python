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

    def __repr__(self):
        return "Student('{}', '{}', '{}')".format(self.firstName, self.lastName, self.studentId, self.remainingAssignments)

    def __str__(self):
        return '{} - {}'.format(self.fullName(), self.email)

    def __add__(self, other):
        return self.remainingAssignments + other.remainingAssignments

    def __len__(self):
        return len(self.fullName())


s_1 = Student('Fahadh', 'Fullbuster', 'b190853cs', 2)
s_2 = Student('Majidh', 'Master', 'b210853cs', 1)

print(s_1)

print(repr(s_2))
print(str(s_2))

print(s_1.__repr__())
print(s_1.__str__())

print("Some more Examples")
print(1+2)
print(int.__add__(1, 2))  # Above line and this are same
print('a'+'b')
print(str.__add__('a', 'b'))  # Above line and this are same
print(len('Fahadh'))
print('Fahadh'.__len__())

print("Sum of two students remaining Assignments")
print(s_1 + s_2)

print("Len of fullName")
print(len(s_2))
