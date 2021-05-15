class Student:
    # instance self as first argument
    def __init__(self, firstName, lastName, studentId, remainingAssignments):
        self.firstName = firstName  # self.firstName can be any thing like self.fName
        self.lastName = lastName
        self.studentId = studentId
        self.remainingAssignments = remainingAssignments
        self.email = firstName + '_' + studentId + '@nitc.ac.in'

    @property
    def batch(self):
        return ('{}{}{}'.format(self.studentId[7], self.studentId[8], self.studentId[9]))

    @property
    def fullName(self):
        return ('{} {}'.format(self.firstName, self.lastName))

    @fullName.setter  # changed firstName and LastName using fullName
    def fullName(self, name):
        first, last = name.split(' ')
        self.firstName = first
        self.lastName = last

    @fullName.deleter  # deleted firstName and LastName using fullName
    def fullName(self):
        print('Delete Name!')
        self.firstName = None
        self.lastName = None


s_1 = Student('Fahadh', 'Fullbuster', 'b190853cse', 2)
s_2 = Student('Majidh', 'Master', 'b210853cse', 1)

print(s_1.firstName)
print(s_1.email)
print(s_1.fullName)
print(s_1.batch)

s_1.firstName = "Fahad"
s_1.studentId = "b190853CSE"

print(s_1.firstName)  # firstName in email is not changing
print(s_1.email)
print(s_1.fullName)
print(s_1.batch)  # batch is changing with out paranthesis

s_1.fullName = 'Fahadh Kasala'

print(s_1.firstName)
print(s_1.email)
print(s_1.fullName)
print(s_1.batch)

del s_1.fullName
