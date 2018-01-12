import  socketserver
from  time import ctime

class CustomResuestHandler(socketserver.BaseRequestHandler):
    def handle(self):
        print('client :', self.client_address)
        ts = ctime().encode('ascii') #unicode string into bype string
        self.request.send(ts)

class DateandTimeService:
    def __init__(self, hostname, port):
        self.server = socketserver.TCPServer((hostname, port), CustomResuestHandler)
        self.server.serve_forever()

if __name__ == '__main__':
    DateandTimeService('localhost', 9999)