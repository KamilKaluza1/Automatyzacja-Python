import pyperclip


text = pyperclip.paste()

# :rozdzielic poszczególne wiersze i dodać gwiazdki''
lines = text.split('\n')
for i in range(len(lines)):
    lines[i] = '* ' + lines[i]
text = '\n'.join(lines)
pyperclip.copy(text)