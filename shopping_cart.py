
available_items = {
    'apple': 2,
    'banana': 1,
    'orange': 2,
    'melon': 4,
    'peach': 5,
    'strawberry': 0.5,
    'cherry': 0.7
}

selected_items = ""
total_amount = 0
print('''
Item Name = Price:
apple = 2 Rs.
banana = 1 Rs.
orange = 2 Rs.
melon = 4Rs.
peach = 5 Rs.
strawberry = 0.5 Rs
cherry = 0.7 Rs

''')
while True:

    print(f'Your bill amount is: {total_amount}\n')
    selected_item = input("Type item name to purchase an item: ")
    selected_quantity = int(input(f'Select quantity of {selected_item}: '))
    #print(available_items[selected_item])
    total_amount = total_amount + available_items.get(selected_item) * selected_quantity
    want_to_continue = input("Do you want to buy more fruits (y/n): ")
    if want_to_continue.lower() != 'y':
        print(f'\n\nThank you for shopping with us.\n')
        print(f'Your total bill amount is: {total_amount}')
        break

