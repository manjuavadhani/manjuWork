import paramiko
class CustomSSHClient:
    def __init__(self, host, port=22, user=None, passwd=None):
        self.ssh = paramiko.SSHClient()
        self.ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        self.ssh.connect(host, port, user, passwd)

    def check_output(self, cmd):
        stdin, stdout, stderr = self.ssh.exec_command(cmd)
        return stdout.read().decode('ascii')

    def __del__(self):
        self.ssh.close()

if __name__ == '__main__':
    ssh = CustomSSHClient('10.110.76.137', 22, 'root', 'pancake')
    print(ssh.check_output('ls -la'))
