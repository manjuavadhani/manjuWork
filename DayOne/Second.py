"""
PackageMnanager

__name
version

__init__()
get_information()
"""
class PackageManager:
    """
    this is doc
    """
    __name = None
    version = None
    def __init__(self, *args):
        if len(args) == 2:
            self.__name = args[0]
            self.version = args[1]

    def get_information(self):
        print('__name: ' ,self.__name)
        print('version: ', self.version)

pmobj = PackageManager('python','3.6')
pmobj.get_information()
print(dir(pmobj))
print(pmobj.__dict__)
print(pmobj.__hash__)
#print(pmobj.__name)