class Demo:
    def __init__(self):
        print(self, 'I am cunst')
    def __del__(self):
        print(self, 'I am dest')

d = Demo()
print (d)