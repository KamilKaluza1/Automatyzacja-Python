import re
led = '#'
txt = '                   ><   przykładowy ciąg textowy   ## '
wo = re.compile(r'[a-zA-Złóźżśćą#<>]+')
mo = wo.findall(txt)
txt = ' '.join(mo)
print(txt)