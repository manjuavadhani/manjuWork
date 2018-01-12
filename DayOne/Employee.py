from DayOne.Person import Person

class Employee(Person):
    def __init__(self,emp,fname,lname):
        self.emp = emp
        super().__init__(fname,lname)

    def get_info(self):
        print('Employee Id is ' , self.emp)
        super().get_info()


if __name__ == '__main__':
    emp = Employee('1234','raja', 'raja')

    emp.get_info()
    print(Employee.mro())