class Raja:
    def pme(self):
        print('I am Raja')


class mantri:
    def pme(self):
        print('I am mantri')


class Rani(mantri):
    def pme(self):
        print('I am Rani')

class yuvaraja(Rani, Raja):
    def pme(self):
        super().pme()


if __name__ == '__main__':
    yuvaraja().pme()
    print(yuvaraja.mro())