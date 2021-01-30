while True:
    max_num = 134
    table_num = int(input("Type a number: "))


    if not isinstance(table_num, int):
        print('please provide a number')
        exit(1)
    elif table_num > max_num:
        print(f'please provide a number between 1 and {max_num}')
        exit(1)

    for a in range(1, 11):
        print(table_num, 'x', a, '=', table_num * a)

    user_ans = input("Do you want to continue(y/n): ")
    if user_ans.lower() == 'n':
        print("Thanks for playing..")
        exit(0)
    elif user_ans != 'y' or user_ans != 'y':
        print("please type y or n")


