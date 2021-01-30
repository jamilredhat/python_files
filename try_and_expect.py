try:
    a = int(input('Type a number: '))
    print(a / 9)
except ZeroDivisionError:
    print("Divided with zero is not allowed.")
except ValueError:
    print("Only numbers are allowed.")
