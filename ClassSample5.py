import gc

class Employee1:
    '''This is the employee class '''


percent_raise = 1.75  # class variable
num_emp = 0


def __init__(self, fname, lname, sal):
    self.fname = fname  # instance variable
    self.lname = lname
    self.sal = sal
    self.email = fname + '.' + lname + '@abc.com'
    Employee1.num_emp += 1


def fullname(self):
    return '{}{}'.format(self.fname, self.lname)


def raise_sal(self):
    self.sal = int(self.sal * self.percent_raise)


class developer(Employee1):
    percent_raise = 1.20


def __init__(self, fname, lname, sal, p_lang):
    super().__init__(fname, lname, sal)
    self.p_lang = p_lang


emp1 = developer('sheeba', 'George', 350000, 'python')
# emp2=Employee('Prem','Kumar',550000)
print(emp1.email)
print(emp1.fullname())
print(emp1.sal)
emp1.raise_sal()
print(emp1.sal)
print(emp1.percent_raise)
print(emp1.p_lang)
# print(emp2.fullname())
# emp2.raise_sal()
# print(emp2.sal)
print("Employee1.__doc__:", Employee1.__doc__)
print("Employee.__name__:", Employee1.__name__)
print("Employee.__module__:", Employee1.__module__)
print("Employee.__bases__:", Employee1.__bases__)
print("Employee.__dict__:", Employee1.__dict__)


