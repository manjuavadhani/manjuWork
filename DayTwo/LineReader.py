import pickle
from pprint import pprint as pp
class Linereader:
    lineN =0
    def __init__(self, fileN):
        self.fileN = fileN
        self.fileH = open(self.fileN, 'rb')

    def reader(self):
        self.lineN += 1
        line = self.fileH.readline()
        print('{}:{}'.format(self.lineN, line))

    def __getstate__(self):
        temp_dict = self.__dict__.copy()
        #del temp_dict['fileH']
        temp_dict.pop('fileH')
        pp(temp_dict)
        return temp_dict

if __name__ == '__main__':
    lr = Linereader(r'C:\Users\ramacm4\PycharmProjects\PythonLearning\DayTwo\CopyInfo.py')
    for x in range(3):
        lr.reader()
    pickle.dump(lr, open('lr.pickle','wb'))
    print()
    print()
    out = pickle.load(open('lr.pickle','rb'))
    print(out)

