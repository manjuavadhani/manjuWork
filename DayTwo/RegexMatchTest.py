###############My CODE###############
# import re
# from os import listdir
# from os.path import isfile,join
#
# directory = 'C:\\Users\\ramacm4\\PycharmProjects\\PythonLearning\\DayOne'
# pattern = r'import'
# for fil in listdir(directory):
#     ab_fi = join(directory, fil)
#     if isfile(ab_fi):
#         with open(ab_fi, 'r') as fh:
#             s = fh.read()
#         mat = re.search(pattern,s)
#         if mat:
#             print(fil , mat.group())

import  re
from fileinput import input, filelineno, filename

def domatch(pattern, *args):
    for line in input(args):
        if re.search(pattern,line, re.I):
            print(filename(), filelineno(), line)

domatch(r'import','C:\\Users\\ramacm4\\PycharmProjects\\PythonLearning\\DayOne\\DirList.py' )

