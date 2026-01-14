class Person:
    def __init__(self, n):
        self._n = n

    def get_role(self):
        return "Person"


class Student(Person):
    def __init__(self, n, i):
        super().__init__(n)
        self.i = i

    def get_role(self):
        return "Student"


p = Person("Alex")
s = Student("Dana", 101)

print(p.get_role())
print(s.get_role())
