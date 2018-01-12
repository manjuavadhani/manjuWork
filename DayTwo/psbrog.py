class Brog:
    __shared_state ={}
    def __init__(self):
        self.__dict__ = self.__shared_state
        self.state = 'Init'

    def __str__(self):
        return self.state

class YourBorg:
    pass

if __name__ == '__main__':
    rm1 = Brog()
    rm2 = Brog()

    rm1.state = 'run'
    rm1.state = 'idle'
    print(rm1.state)
    print(rm2.state)