while True:
    if input('kim jesteś?') != 'Janek':
        continue
    password = input('witaj janek, podaj hasło (ryba)')
    if password == 'miecznik':
        break
print("you have access")