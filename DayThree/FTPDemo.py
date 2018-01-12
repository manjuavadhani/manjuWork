import ftplib
import zipfile
from glob import glob


class ArchiveMe:
    def __init__(self, zipname, *args):
        self.zipname = zipname
        self.contents = args
        self.__zipme()

    def __zipme(self):
        zf = zipfile.ZipFile(self.zipname, 'w')
        for items in self.contents:
            zf.write(items)
        zf.close()



class FTPDemo:
    def __init__(self, host, port=21,user=None, psswa=None):
        self.ftpc = ftplib.FTP()
        self.ftpc.connect(host,port)
        self.ftpc.login(user,psswa)

    def list_content(self):
        self.ftpc.retrlines('LIST')

    def putfile(self, toPut):
        cmd = "STOR {}".format(toPut)
        self.ftpc.storbinary(cmd , open(toPut, 'rb'))
        print('Done uploading file {}'.format(toPut))


    def __del__(self):
        self.ftpc.close()

if __name__ == '__main__':
    ftpob = FTPDemo('10.110.75.214')
    ftpob.list_content()

    currentDirfiles = glob(r'C:\Users\ramacm4\PycharmProjects\PythonLearning\DayOne\*')
    print(currentDirfiles)
    zipme = ArchiveMe('zipme.zip',*currentDirfiles)

    ftpob.putfile('zipme.zip')