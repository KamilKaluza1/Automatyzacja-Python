import random

secretNumber = random.randint(1, 20)
print("mam na myśli pewną liczbę zgaduj")

for guessTaken in range(1, 7):
    guess = int(input('podaj liczbę: '))

    if guess > secretNumber:
        print('Za duża')
    elif guess < secretNumber:
        print('za mała')
    else:
        break
if secretNumber == guess:
    print("gratulacje to ta")
else:
    print("przegrałeś")