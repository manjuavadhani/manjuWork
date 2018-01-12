class Person:
    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname

    def get_info(self):
        print('First Name is ', self.fname )
        print('Last Name is ', self.lname)
if __name__ == '__main__':
    per = Person('manjunath', 'ramachandra')
    per.get_info()