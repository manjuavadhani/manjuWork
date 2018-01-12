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
from os.path import getmtime, getsize, isfile, isdir,join
from time import ctime
from pprint import pprint as pp
class DirectoryListing:

    def __init__(self, *args):
        self._input_dir = args
        print('Input directories are ' , self._input_dir)

    def listing(self, di):
        content = {}
        for f in listdir(di):
            abs_path = join(di, f)
            if isfile(abs_path):
                content.setdefault(di, {})[f]= [self.getSizeAndtime(abs_path)]
            if isdir(abs_path):
                self.listing(abs_path)
        return content

    def getSizeAndtime(self, fileN):
        return [getsize(fileN), ctime(getmtime(fileN))]

    def getDirFiles(self):
        finalist = dict()
        for di in self._input_dir:
            finalist = {di:self.listing(di)}
        pp(finalist)



ob = DirectoryListing('C:\MandMMarriage')
ob.getDirFiles()
# print(ob.listing())