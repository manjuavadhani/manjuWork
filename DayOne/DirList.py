"""
{
'd1': {
        'f1': [size, modified_time],
        'f2': [size, modified_time],...
        }
'd2': {
        }
}
"""

from os import listdir
from os.path import getmtime, getsize, isfile, isdir,join,basename
from time import ctime
from pprint import pprint as pp

class DirectoryListing:
    content = dict()
    def __init__(self, *args):
        self._input_dir = args
        print('Input directories are ' , self._input_dir)
        self.__dirlisting()


    def __dirlisting(self):
        for x in self._input_dir:
            file_names = [join(x, item) for item in listdir(x) if isfile(join(x, item))]

            for fileN in file_names:
                bfname = basename(fileN)
                self.content.setdefault(x, {})[bfname] = self.getSizeAndtime(fileN)

    def getSizeAndtime(self, fileN):
        return [getsize(fileN), ctime(getmtime(fileN))]

if __name__ == '__main__':

    obj = DirectoryListing('C:\E', 'c:\python27\scripts')
    pp(obj.content)