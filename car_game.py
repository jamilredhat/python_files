is_started = False
user_command = ""

while True:
    user_ans = input("Type a command OR type help to get list of commands: ")

    if user_ans == 'quit':
        print('Exiting')
        break
    elif user_ans == 'start' and is_started == True:
        print('Car is already started')
    elif user_ans == 'start' and is_started == False:
        print('Car started..')
        is_started = True
    elif user_ans == 'stop' and is_started == True:
        print('Stopping car...')
        is_started = False
    elif user_ans == 'stop' and is_started == False:
        print('Car is already stopped')
    elif user_ans == 'help':
        print('''
help        To print this message.
quit        To exit game.
start       To start the car.
stop        To stop the car.
        ''')
    else:
        print('Please type "help" to find correct options.')
