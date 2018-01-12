import re

class RegexmatchEx:
    def example1(self):
        mystring = 'I am  python guy and perl'
        pattern = '.+?u'
        m = re.search(pattern, mystring, re.IGNORECASE)
        print(m)
        if m:
            print('Match found', m.group())
            print(mystring[:m.start()])
            print(mystring[m.end():])
        else:
            print('Not found')

    def example2(self):
        mystring = '11-01-2018 09:53:20 at the log'
        pattern = r'(\d{2}-\d{2}-\d{4})\ (\d\d:\d\d:\d\d)'
        m = re.search(pattern, mystring, re.IGNORECASE)
        print(m)
        if m:
            print('Match found', m.group(), m.group(1), m.group(2), m.groups())
        else:
            print('Not found')

if __name__ == '__main__':
    re1 = RegexmatchEx()
    re1.example1()
    re1.example2()
