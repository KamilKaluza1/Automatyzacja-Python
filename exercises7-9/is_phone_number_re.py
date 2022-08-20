import re

message = 'Zadzwoń pod numer 415-555-1111 po przerwie.'
phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
mo = phoneNumRegex.search(message)
print(f"znalezoiono: {mo.group()}")