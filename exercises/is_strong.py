
import re
pas = 'jdgfA1ddd1kyd'
iseight = re.compile(r'\w{8}(\w)*')
isbig = re.compile(r'[A-Z]')
issmall = re.compile(r'[a-z]')
isdec = re.compile(r'\d')



def is_strong(pas):
    mo1 = isbig.search(pas)
    mo2 = iseight.search(pas)
    mo3 = issmall.search(pas)
    mo4 = isdec.search(pas)
    if mo1 == None:
        print("hasło nie ma dużej litery")
    elif mo2 == None:
        print("hasło nie ma wymaganej ilości znaków")
    elif mo3 == None:
        print("hasło nie ma małej litery")
    elif mo4 == None:
        print("hasło nie ma cyfry")
    else:
        print('Password is strong')


is_strong('jdgfdddkyd')
