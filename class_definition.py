
class TestClass:

    def __init__(self, price, total):
        TestClass.price = price
        TestClass.total = total

    def print_message(self, message):
        print(message)

    def write_message(self):
        print("Hi there. I am in write_message function of class TestClass")


test = TestClass(400, 700)

test.write_message()
test.print_message("Hi this is print_message function")

print(test.price)
print(test.total)
