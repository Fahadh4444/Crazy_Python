import datetime


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

    @classmethod
    # wont take instance as argument, they take class as argument
    def setAssignments(cls, assignments):
        cls.newAssignments = assignments

    @classmethod
    def from_string(cls, s_str):
        firstName, lastName, studentId, remainingAssignments = s_str.split('-')
        return cls(firstName, lastName, studentId, remainingAssignments)

    @staticmethod
    def isHoliday(day):
        if day.weekday() == 5 or day.weekday() == 6:
            return True
        return False


s_1 = Student('Fahadh', 'Fullbuster', 'b190853cs', 2)
s_2 = Student('Majidh', 'Master', 'b210853cs', 1)

Student.setAssignments(10)
print(Student.newAssignments)
print(s_1.newAssignments)
print(s_2.newAssignments)

s_3 = Student.from_string('Yesh-Chala-b180853cs-3')
print(s_3.fullName(), s_3.email)

myDate = datetime.date(2019, 10, 29)
print(Student.isHoliday(myDate))
