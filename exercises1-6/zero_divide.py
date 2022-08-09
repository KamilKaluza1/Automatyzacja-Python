def spam(divideby):
    try:
        return 42 / divideby
    except ZeroDivisionError:
        print("Nie dziel przez 0")

print(spam(0), spam(1))