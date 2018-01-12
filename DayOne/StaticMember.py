class MaxReach(Exception):
    pass

class StaticMemberDemo:
    counter = 0
    max_limit = 4
    def __init__(self):
        StaticMemberDemo.counter += 1
        StaticMemberDemo.checkForError()
    @staticmethod
    def checkForError():
        if StaticMemberDemo.counter > StaticMemberDemo.max_limit:
            raise MaxReach ('Sorry Max limit reached')

    #checkForError = staticmethod(checkForError)

if __name__ == '__main__':
    for x in range(9):
        c1 = StaticMemberDemo()
        # print(c1.counter)
        # c2 = StaticMemberDemo()
        # print(c2.counter)
