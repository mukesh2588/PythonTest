class Employee:
    perc_raise=1.05
    raise_amount = 1.03
    def  __init__(self,first_name,last_name,sal):
        self.first_name = first_name
        self.last_name=last_name
        self.sal = sal
        self.email = first_name + '.' + last_name + '@company.com'
        self.__mobile = 9345677987
    def  fullname(self):
        return '{}{}'.format(self.first_name,self.last_name)
    def apply_raise(self):
        self.sal=int(self.sal* self.perc_raise)

e1 = Employee("rajat","yadav",33000)
e2 = Employee("sushma","mohan",45000)

print(e1.apply_raise())

