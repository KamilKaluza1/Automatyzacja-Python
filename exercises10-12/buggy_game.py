import random
guess = ''
while guess not in ('orzeł', 'reszka'):
    print('Odgadnij wynik rzutu monetą! Wpisz orzeł lub reszka:')
    guess = input()
toss = random.randint(0, 1) # 0 oznacza reszkę, natomiast 1 to orzeł.
if toss == guess:
    print('Odgadłeś!')
else:
    print('Nie udało się! Spróbuj ponownie!')
    guesss = input()
    if toss == guess:
        print('Odgadłeś!')
    else:
        print('Nie udało się! Naprawdę kiepsko Ci dziś idzie.')