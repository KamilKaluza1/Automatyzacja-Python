import re

led = '#'
txt = '                   ####   przykładowy# ciąg textowy   ##### '


def re_strip(txt, led=''):
    wo = re.compile(r'[a-zA-Złóźżśćą#<>]+')
    mo = wo.findall(txt)
    print(mo)
    txt = ' '.join(mo)
    done = re.sub(f"(^{led}*)|({led}*$)",'', txt)
    print(done)

re_strip(txt,led)
