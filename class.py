# wap to create a class named employee having attribute name, eid, salary, department, promotion, working days\
# behaviour: salary(), promotion(), display(), change_department()\
# behaviour can modify attribute\

class Employee:
  def __init__(self):   # __init__ it is a constructor in python for class
    self.name = input("Enter Name")
    self.eid = int(input("Enter Employee Id"))
    self.sal = int(input("Enter Employee Salary"))
    self.dep = input("Enter Employee Department")
    self.working_days = int(input("Enter Working Days"))
  def display(self):
    print("Eployee Name: ",obj.name)
    print("Employee Id: ",obj.eid)
    print("Employee Salary",obj.sal)
    print("Employee Department",obj.dep)
    print("Working Days",obj.working_days)

obj = Employee()
obj.display()


class A:
    def f2(self):
        print("Class A")
class B:
    def f2(self):
        print("Class B")

class C(A,B):
    def f3(self):
        pass
    def ck(self):
        B.f2(self)  
k = C()
B.f2(k)
k.ck()