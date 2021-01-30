
# A function that does not take any argument.

def print_message():
    print("Hi There")


# Calling function.

print_message()

# A function that takes an argument.


def print_argument(message):
    print(message)


print_argument("This is test message")

# Giving argument a name.

def print_arguments(any_string, any_number):
    print(f'{any_string} and {any_number}')


print_arguments("This is test", 50)
# we can also call it like
print_arguments(any_string="This is test message", any_number=55)

