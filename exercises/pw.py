import sys, pyperclip

#! python 3
#pw.py not (save) to use password manager

PASSWORDS = {
    'email': 'F7minlBDDuvMJuxESSKHFhTxFtjVB6',
    'blog': 'VmALvQyKAxiVH5G8v01if1MLZF3sdt',
    'luggage': '12345'
    }


if len(sys.argv) <2:
    print("Użycie: python pw.py [konto] -skopiowanie hasła wskazanego konta")
    sys.exit()

account = sys.argv[1]

if account in PASSWORDS:
    pyperclip.copy(PASSWORDS[account])
    print(f"hasło do konta {account} zostało skopiowane do schowka.")
else:
    print(f"nie istnieje konto o nazwie {account}.")