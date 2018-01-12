import pyexcel
import threading
from DayThree.SSHDemo import CustomSSHClient

target_file = 'response.txt'

class ThreadSShClient:
    def __init__(self, hostname, port,user, passwd, job, lock):
        self.host = hostname
        self.ssh = CustomSSHClient(hostname, port, user, passwd)
        self.command =job
        self.lock = lock
        self.__ssh_handler()

    def __ssh_handler(self):
        payload = self.ssh.check_output(self.command)
        t_name = threading.current_thread().getName()
        with self.lock:
            with open(target_file, 'a') as fw:
                fw.write("{} ran {} @{}\n".format(t_name,self.command,self.host))
                fw.write('-' * 60+ "\n")
                fw.write(payload)
                fw.write("\n")

def main():
    list_threads = list()
    lock = threading.Lock()
    for row in pyexcel.get_sheet(file_name='hosts.xlsx'):
        t = threading.Thread(target=ThreadSShClient, args=row + [lock])
        list_threads.append(t)
        t.start()

    for t in list_threads:
        t.join()

if __name__ == '__main__':
    main()
