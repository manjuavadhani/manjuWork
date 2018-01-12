from DayOne.DirList import DirectoryListing
from json import dump

class DirTwoList(DirectoryListing):
    def to_json(self,json_file):
        try:
            dump(self.content, open(json_file, 'w'), indent=5)
        except (FileNotFoundError, IOError) as error:
            print(error)

if __name__ == '__main__':
    DirTwoList('c:\E', 'c:\python27\scripts').to_json('myjson.json')
