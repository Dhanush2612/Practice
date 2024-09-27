#Method 1
class Student:
    def __init__(self,no,name,sub):
        print('No.:',no)
        print('Name:', name)
        print('Subject:', sub)
    def display(self,no,name,sub):
        print('No.:', no)
        print('Name:', name)
        print('Subject:', sub)

s1 = Student(1,'Dhanush','CSE')
s1.display(2,'Ram','AI')

#Method 2
class Student:
    def __init__(self,no,name,sub):
        print(f'No.:{no} Name:{name} Sub:{sub}')
    def display(self,no,name,sub):
        print(f'No.:{no} Name:{name} Sub:{sub}')

s1 = Student(1,'Dhanush','CSE')
s1.display(2,'Ram','AI')