import multiprocessing
from os import getpid

def task_set():
    p_name = multiprocessing.current_process().name
    p_id = multiprocessing.current_process().ident
    print('{} : {}'.format(p_name, p_id))

def main():
    pid = getpid()

    print('parent process id : {}'.format(pid))

    for item  in range(5):
        p = multiprocessing.Process(target=task_set())