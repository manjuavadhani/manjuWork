import subprocess

output = subprocess.check_output('ipconfig')
print(output.decode('ascii'))