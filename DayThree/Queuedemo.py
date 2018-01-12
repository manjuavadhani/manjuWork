import threading
import logging
from queue import Queue
import requests

format_str = "%(threadName)s: %(message)s"
logging.basicConfig(level=logging.DEBUG, format=format_str)

def taskInfo(q):
    myurl = q.get()
    data = requests.get(myurl).content[:64]
    logging.info(data)
    q.task_done()

def main():
    urls =['http://python.org', 'http://linux.org', 'http://kernal.org']
    q_obj = Queue()

    for url in urls:
        t = threading.Thread(target=taskInfo , args=(q_obj,))
        t.start()
    for url in urls:
        q_obj.put(url)

    q_obj.join()
    print('test me')

if __name__ == '__main__':
    main()