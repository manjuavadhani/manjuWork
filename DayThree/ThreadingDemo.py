import threading
import time

class Task:
    def worker(self):
        r_name = threading.current_thread().getName()
        t_id = threading.current_thread().ident
        time.sleep(2)
        print('{}:{}\n'.format(r_name,t_id))

def main():
    task_obj = Task()
    list_threads = list()
    for item in range(1,6):
        t = threading.Thread(target= task_obj.worker, name='t{}'.format(item))
        #t.setName('t{}'.format(item))
        list_threads.append(t)
        t.start()
    for t in list_threads:
        t.join()

    print('main thred terminates')

if __name__ == '__main__':
        main()