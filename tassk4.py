class Employee:
    def __init__(self, s):
        self._s = s

    def get_salary(self):
        return self._s

    def get_role(self):
        return "Employee"


class Manager(Employee):
    def get_role(self):
        return "Manager"

    def get_bonus(self):
        return self._s * 0.2


def f(e):
    for i in e:
        print(i.get_role(), i.get_salary())


e1 = Employee(1000)
e2 = Manager(2000)

f([e1, e2])
