class ListManager:
    students_CET = set(["Vishal", "Rohan", "Jay", "David", "Eva", "Pooja", "Dev"])
    students_JEE = set(["Vishal", "Jay", "Kiran", "Pooja", "Hena", "Ivy"])
    students_NEET = set(["David", "Eva", "Jay", "Kiran", "Neha", "Vishal"])

    def union_student(self):
        union_students = self.students_CET.union(self.students_JEE, self.students_NEET)
        print("Students enrolled in at least one exam (Union):")
        print(union_students)

    def intersection_student(self):
        intersection_students = self.students_CET.intersection(self.students_JEE, self.students_NEET)
        print("\nStudents enrolled in all three exams (Intersection):")
        print(intersection_students)

    def difference_student(self):
        only_CET_students = self.students_CET.difference(self.students_JEE, self.students_NEET)
        print("\nStudents enrolled only in CET (Difference):")
        print(only_CET_students)


obj = ListManager()

while True:
    n = int(input('1.Union \n2.Intersection\n3.Difference\n4.Exit : '))

    if n == 1:
        obj.union_student()
    elif n == 2:
        obj.intersection_student()
    elif n == 3:
        obj.difference_student()
    else:
        break


s = {4, 5, 6, 7}
print(type(s))

s = set((4, 5, 6, 7))
print(type(s))
