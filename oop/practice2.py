class Employee:
    
    def __init__(self, first_name, last_name, employee_pay):
        self.firstname = first_name
        self.lastname = last_name
        self.pay = employee_pay
        self.email = last_name + first_name + '@gmail.com'
        self.raise_amount = 1.10
    def full_name (self):
        return self.firstname + ' ' + self.lastname
    def pay_raise (self):
       self.pay = int(self.pay * self.raise_amount)
       return self.pay
class Receptionist (Employee):
    def __init__(self, first_name, last_name, employee_pay):
        super().__init__(first_name, last_name, employee_pay)
        self.raise_amount = 1.20
    def name (self):
        return f"Your name is {self.firstname} {self.lastname}."
class Developers (Employee):
    def __init__(self, first_name, last_name, employee_pay):
        super().__init__(first_name, last_name, employee_pay)
        self.raise_amount = 1.50
class Electricians (Employee):
    def __init__(self, first_name, last_name, employee_pay):
        super().__init__(first_name, last_name, employee_pay)
        self.raise_amount = 1.35
class Nurses (Employee):
    def __init__(self, first_name, last_name, employee_pay):
        super().__init__(first_name, last_name, employee_pay)
        self.raise_amount = 1.44
employee1 = Developers('Alex', 'Guandaru',50000)
employee2 = Electricians('Michael', 'Macharia',40000)
employee3 = Nurses('Eunice', 'Muchina', 30900)
employee4 = Receptionist('Grace', 'Mbugua', 46000)


#polymorphism
EMPLOYEES = [employee1, employee2,employee3,employee4]
for employee in EMPLOYEES:
    print(employee.pay)
    print(employee.pay_raise())
    print(employee.full_name())
    print(employee.email)
    print()

