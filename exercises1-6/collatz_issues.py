def collatz(value):
    while value != 1:
        if value % 2 == 0:
            print(int(value))
            value = value / 2
        else:
            print(int(value))
            value = value * 3 + 1
    print(int(value))



try:
    collatz(int(input("Podaj wartość")))
except ValueError: 
    print('podana wartość musi być liczbą całkowitą')